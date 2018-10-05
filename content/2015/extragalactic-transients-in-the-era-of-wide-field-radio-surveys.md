+++
date = 2015-02-06T18:47:20Z
title = "“Extragalactic Transients in the Era of Wide-Field Radio Surveys”"

[extra]
wp_rel_permalink = "/2015/02/extragalactic-transients-in-the-era-of-wide-field-radio-surveys/"
wp_shortlink = "/?p=930"
+++

Over the past few months I’ve been working on a paper with my adviser
[Edo Berger](http://scholar.harvard.edu/eberger/home) and
[Brian Metzger](http://www.columbia.edu/~bdm2129/) of Columbia, and as of
today it’s submitted to [ApJ](http://iopscience.iop.org/0004-637X/) and
[out on Arxiv](http://arxiv.org/abs/1502.01350)! It’s entitled _Extragalactic
Transients in the Era of Wide-Field Radio Surveys. I. Detection Rates and
Light Curve Characteristics_, and as the title might suggest it connects more
to my doctoral research on radio transients than my more recent work on
magnetism in cool stars and brown dwarfs.

The term “radio transient” generally refers to any astronomical source of
radio emission that appears unexpectedly. Since the definition involves
something new appearing, radio transients are generally associated with
_events_ rather than _objects_. Lots of astrophysical events are known — or
predicted — to result in radio emission, so the set of radio transients
includes many different kinds of phenomena: it is an _astronomical_ definition
rather than an _astrophysical_ one.

But there’s a reason we lump many kind of events into this overarching
category. Up until the past decade or so, it’s been difficult to discover
radio transients of any kind. There are several reasons for this, but one of
the key ones is that fairly basic physical and technical tradeoffs have
historically driven the best-performing radio telescopes to have very small
“fields of view,” meaning that they can only observe small patches of the sky
at once. And if you’re interested in unexpected events that could occur
anywhere in the sky, you have to get pretty lucky to find one when you’re only
ever looking at a tiny little piece of it.

You can’t change the laws of physics, but some of the same technologies that
have driven the digital revolution have also significantly changed the
tradeoffs involved in building radio telescopes. (For more on this, see
[Chapter 1 of my dissertation](/dissertation/).) It’s now possible to build
sensitive telescopes that can see much more of the sky at once than before,
making searches for radio transients much more feasible. In astronomy, new
ways of looking at the sky have almost always been associated with exciting
new discoveries, so this new capability of studying the “time domain” radio
sky has brought a lot of excitement to see what’s out there waiting to be
found. That’s why there are a variety of ongoing and upcoming searches for
radio transients such as [VAST](http://www.physics.usyd.edu.au/sifa/vast/),
[VLASS](https://science.nrao.edu/science/surveys/vlass) (partially), the
[LOFAR RSM](http://www.transientskp.org/), and whatever acronym will
eventually be given to the
[SKA transient surveys](https://www.skatelescope.org/radio-transients/); and
hence the “Era of Wide-Field Radio Surveys” in the title of our paper.

That’s the background. What our paper does is predict what these surveys might
actually find. Our work is the first comprehensive end-to-end simulation of
the search process, modeling the rates and distributions of various events,
their radio emission, and the detection methods that surveys will likely use.

{% figure(src="https://newton.cx/~peter/wp/wp-content/uploads/2015/02/ludlow-lcs-1p3ghz.png") %}
Science! Radio light curves of the various events we consider at 1.3 GHz. A big part of the work in the paper was to find and implement the best-available models for radio emission from a wide variety of astrophysical events.
{% end %}

To keep things tractable, we focused on a particular kind of potential radio
transients — extragalactic synchrotron events. The “extragalactic” means that
the events come from outside the Milky Way, which is usually the genre that
people are most interested in. The “synchrotron” refers to the radio emission
mechanism. For the general group of surveys we consider, all known radio
transients are synchrotron emitters, and I’d argue that it’s hard to concoct
plausible events in which synchrotron will not be the primary emission
mechanism. This is important, because one of the things we show in the paper
is that the synchrotron process brings certain basic restrictions to the kind
of emission you can get. In particular, brighter events generally evolve on
slower timescales, so that something bright enough to be seen from another
galaxy cannot get significantly brighter or dimmer in less than about 100
days. That means that if you’re looking for radio transients, it’s not helpful
to check the same part of the sky more frequently than this pace.

Various other papers have predicted detection rates for these sorts of events,
but many of them have done so in a back-of-the-envelope kind of way. But we
tried to do things right: take into account cosmological effects like
[non-Euclidean luminosity distances](http://en.wikipedia.org/wiki/Luminosity_distance)
and [K-corrections](http://en.wikipedia.org/wiki/K_correction), use
best-available radio emission models, and model the actual execution of a
given survey. Doing this brought home a point that I’d say has been
insufficiently appreciated: if you observe more frequently than the 100-day
timescale mentioned above, typical back-of-the-envelope calculations will
overestimate your survey’s efficacy. (If you do this you can recover some
power by averaging together multiple visits, but in most cases it’s better to
cover more sky rather than to revisit the same spot.)

Overall, we predict that few (dozens) radio transients will be found until the
advent of the [Square Kilometer Array](http://skatelescope.org/). Several of
the choices that lead to this result are on the conservative side, but we feel
that that’s justified — historically, radio transient surveys have turned up
more false positives than real events, and you’re going to need a robust
detection to actually extract useful information from an event. This is
particularly true because radio emission generally lags that in other bands,
so if you discover something in the radio, you have poor chances of being able
to learn much about it from, say, optical or X-ray emission. This is
unfortunate because it can be quite hard to learn much from radio observations
without the context established from data at shorter wavelengths. We’ll pursue
this idea in a follow-up paper.

There’s quite a lot more to [the paper](http://arxiv.org/abs/1502.01350) (… as
you’d hope …) but this post is awfully long as it is. Overall, I’m very happy
with our work — people have treated this topic handwavily for a while, and
it’s finally getting the detailed treatment it deserves. The process of
writing the paper was also rewarding: this happens to be the first one I’ve
been on in which more than one person has had a heavy hand in the manuscript.
(I’d call it a coincidence, but in my prior experiences the writing has been
more-or-less entirely one person’s responsibility.) The mechanics of
collaborative writing are still awkward — hence upstart websites like
[Overleaf](https://www.overleaf.com/) or
[ShareLatex](https://www.sharelatex.com/) — but that aspect made it feel like
more of a team project than other work I’ve done so far. I’ll be spearheading
the follow-up paper, so there should be more of this feeling in my future!
