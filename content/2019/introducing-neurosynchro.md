+++
date = 2019-05-09T09:32:30-04:00
title = "Fast synchrotron calculations with neural networks: neurosynchro"
+++

It’s a truism in science that when you set out to solve big, inspiring
questions you will soon find yourself mired in the technical details of some
preposterously obscure topic. That’s surely the case for my work — while the
main thrust of my astrophysics research is to study the magnetic fields of
other stars and planets, one of the things I’ve been trying to think about a
lot lately is the
[efficient computation](https://en.wikipedia.org/wiki/Program_optimization) of
[numerical parameters](https://en.wikipedia.org/wiki/Numerical_method) for
[polarized](https://en.wikipedia.org/wiki/Polarization_(waves))
[synchrotron](https://en.wikipedia.org/wiki/Synchrotron_radiation)
[radiative transfer](https://en.wikipedia.org/wiki/Radiative_transfer). So it
goes.

One of the tradeoffs of [my new job](./2018/operation-innovation.md) is that I
have a lot less time for doing astrophysics research myself, so this work is
moving forward slowly these days. But I did manage to make something neat last
year, and now I have time to write about it! It’s
[neurosynchro](https://neurosynchro.readthedocs.io/), an open-source Python
package for training and using neural networks to compute approximate
synchrotron radiative transfer coefficients. You can jump right into
[a tutorial](https://neurosynchro.readthedocs.io/en/latest/index.html#tutorial-aka-how-to-use-it),
[installation instructions](https://neurosynchro.readthedocs.io/en/latest/installation.html),
and [the GitHub repository](https://github.com/pkgw/neurosynchro/).

<!-- more -->

The basic problem that [neurosynchro](https://neurosynchro.readthedocs.io/) is
trying to help solve is
[polarized](https://en.wikipedia.org/wiki/Polarization_(waves))
[synchrotron](https://en.wikipedia.org/wiki/Synchrotron_radiation)
[radiative transfer](https://en.wikipedia.org/wiki/Radiative_transfer). Let’s
break it down:

- The *synchrotron* process is a phenomenon in which energetic particles
  interact with magnetic fields to create light. It turns out that in
  astrophysics, the synchrotron process is a fairly common source of light in
  the radio portion of the spectrum (AKA radio waves). Analyzing the
  observations of synchrotron emission can tell us about the particles and
  magnetic fields that created it, which is often something we care about.
- The light created by the synchrotron process is often *polarized* in complex
  ways. The polarization properties of the emission are an important source of
  information about what’s going on, but the computations needed to predict
  the polarization are tricky.
- Finally, the *radiation* (light) created by the synchrotron process has to
  travel to us from its source, and its properties can change dramatically as
  it *transfers* through various space plasmas — including its polarization
  properties. In order to relate what we observe to what was emitted, we have
  to have a model of what’s in between and to calculate how the radiation
  properties evolve as it propagates.

Why might you care about all this? One prominent example is if you’re in the
business of
[making images of black hole shadows](https://iopscience.iop.org/journal/2041-8205/page/Focus_on_EHT)
like the [Event Horizon Telescope](https://eventhorizontelescope.org/) just
did! The black hole itself emits no light, but the relativistic plasma around
it does — via the synchrotron process. It’s cool to take the picture, but to
actually get scientific insight from the data, you need software for polarized
synchrotron radiative transfer to connect the data to a model.

When you design such software, you can basically break the problem into three
pieces. First, you need a model of what the magnetic fields and particles are
like. Second, at each point between you and the radiation, you need to
calculate eight special numbers that describe the how the radition is emitted
and modified. Third, you need to put those numbers into a matrix integral
computation that gives you your final answer.

It turns out that the second step is really tricky. Even in relatively simple
models, each of the eight numbers you need to compute is a double integral
based on complex physics. It’s a whole research effort to write a program to
do these calculations, and the calculations are often slow and finicky. I
would claim that the other two steps are *relatively* straightforward,
although there’s a whole literature on radiative transfer integrators as well.

[Neurosynchro](https://neurosynchro.readthedocs.io/) helps with this second
step. It does *not* do these tricky calculations itself. Instead, it helps you
create a function that can give you an *approximation* to the output of a
detailed calculation, quickly and reliably. So if you have a program that does
one of these calculations, you can have one big session where you generate a
bunch of sample outputs, then use the fast approximation in your transfer
calculations. Compared to my [Rimphony](https://github.com/pkgw/rimphony) code
— which will get a post of its own, sooner or later — neurosynchro can speed
calculations up by a factor of 10,000 while maintaining good accuracy.

How do we generate this approximation? Well, what I’ve described above is
exactly the process of using an
[artificial neural network](https://en.wikipedia.org/wiki/Artificial_neural_network)!
One way of thinking about neural networks is that they are tools for
automatically approximating multi-dimensional functions, which is exactly the
task here. The approximation is “trained” using the outputs of a detailed
calculation program, which is slow. But once that’s done, it’s fast to compute
new answers for arbitrary inputs.

There are two especially tricky parts that neurosynchro takes care of. First,
the numbers that describe the radiative transfer matrix must obey a particular
set of relationships, even as they vary over a wide range of magnitudes.
Neurosynchro automates a group of parameter transformations that both ensure
that you don’t get bogus results, *and* make it much easier for the neural
network training to succeed.

Second, different physical models take different input parameters. In some
cases, you might care about a parameter *p* describing a power-law
distribution of particle energies. In other cases, it might be *θ* describing
a characteristic temperature. Neurosynchro gives you a common framework for
describing these inputs, making it possible to use it as a common interface to
a variety of physical models and detailed synchrotron calculation codes.

I think this is one of the neatest things about neurosynchro. Traditionally,
if you want to use a synchrotron calculation code, you need to install it,
figure out its interface, discover its strengths and weaknesses, and find a
way to apply it to whatever problem you’re trying to solve. With the neural
network approach, this undertaking can instead be broken down into several,
nicely distinct steps:

1. If you’re starting totally from scratch, you need to create a training set
   with your detailed calculation code. Neurosynchro specifies a very simple
   input data format, so no matter what code you’re using it should be very
   easy to generate the training set — you just need to burn a lot of
   CPU-hours. And, crucially, once you’ve created your training set, *you’re
   done*. You don’t need to rerun those slow calculations ever again, and
   other folks don’t need to either! You can share the training data online,
   as I have done for
   [this Rimphony example](https://neurosynchro.readthedocs.io/en/latest/download-training-set.html#download-training-set).
   Now anyone else can use the data as an input for their own neural network.
2. If you want to create your own specialized approximator, you need to
   download or compute a training set. Then you need to describe the structure
   of the data and run the training process, which can take a little while.
   The great thing is that the output of this process is once again a simple,
   portable dataset:
   [here is a network trained on my Rimphony data](https://neurosynchro.readthedocs.io/en/latest/download-trained-networks.html).
   If you want to spend time optimizing the accuracy and behavior of the
   network, you can do it without rerunning the really big computations to
   generate the training data in the first place, and then you can easily
   share the results with others.
3. But if all you care about is getting the eight magic numbers, the only
   thing you need to do is to download a pre-trained network. The data file is
   small (160 kiB for the example above), the resulting computation is
   extremely fast, and the technology is built on popular machine learning
   tools so that the installation is generally easy.

Say, for instance, that someone has developed a whiz-bang new synchrotron
calculator that they claim will solve all of your problems. Historically, it’s
a major investment to try out their code and see how it performs. With
neurosynchro, you just have to download about a megabyte of data and swap out
a file. And did I mention that it can be more than 10,000 times faster than
running the detailed calculations?

I need to write all of this up in a detailed paper where I really dig into the
performance and limitations of this model, but I hope that this will be a
really useful tool in this very, very niche sector. If you do polarized
synchrotron radiative transfer calculations,
[try neurosynchro today!](https://neurosynchro.readthedocs.io/en/latest/installation.html)
