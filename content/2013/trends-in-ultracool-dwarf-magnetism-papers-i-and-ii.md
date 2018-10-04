+++
date = 2013-10-29T15:33:39Z
title = "Trends in ultracool dwarf magnetism: Papers I and II"

[extra]
wp_rel_permalink = "/2013/10/trends-in-ultracool-dwarf-magnetism-papers-i-and-ii/"
wp_shortlink = "/?p=806"
+++

Well, the pair of papers that I’ve been working on for much of this year have
finally hit [arxiv.org](http://arxiv.org/), showing up as
[1310.6757](http://arxiv.org/abs/1310.6757) and
[1310.6758](http://arxiv.org/abs/1310.6758). I’m very happy with how they
turned out, and it’s great to finally get them out the door!  These papers are
about magnetism in very small stars and brown dwarfs, which we refer to as
“ultracool dwarfs” or UCDs. Observations show that UCDs produce strong
magnetic fields that can lead to large flares. However, the internal structure
of these objects is very different than that of the Sun (no [radiative
core](http://en.wikipedia.org/wiki/Sun#Radiative_zone)), in a way that makes
it challenging to develop a theory of how UCDs produce their magnetic fields,
and of what configuration those fields assume.  So we turn to observations for
guidance. Our papers present new observations of seven UCDs made with the
[Chandra space telescope](http://chandra.harvard.edu/), detecting X-rays, and
the recently-upgraded [Very Large
Array](https://science.nrao.edu/facilities/vla), detecting radio waves.
Magnetic short circuits (“[reconnection
events](http://en.wikipedia.org/wiki/Magnetic_reconnection)”) are understood
to lead to both X-ray and radio emission, and observations in these bands have
turned out to provide very useful diagnostics of magnetism in both distant
stars and the Sun.  When people [such as my
boss](http://dx.doi.org/10.1088/0004-637x/709/1/332) started studying UCD
magnetism, they soon discovered that that the radio and X-ray emission of
these small, cool objects has several surprising features when compared to
Sun-like stars. We hope that by understanding these surprising observational
features, we can develop a better theoretical understanding of what’s going on
“under the hood.” This in turn will help us grapple with some challenging
basic physics and also inform our understanding of what the magnetic fields of
extrasolar planets might be like, which has large implications for their
habitability ([e.g.](http://dx.doi.org.ezp-
prod1.hul.harvard.edu/10.1051/0004-6361/201321504)).  [The first
paper](http://arxiv.org/abs/1310.6757) considers the ratio of radio to X-ray
brightness. While this ratio is fairly steady across many stars, in some UCDs
the radio emission is much too bright. [The second
paper](http://arxiv.org/abs/1310.6758) considers X-ray brightness as a
function of rotation rate. UCDs tend to rotate rapidly, and if they were Sun-
like stars this would lead to them having fairly bright X-ray emission
regardless of their precise rotation rate. But instead, they have depressed
levels of X-ray emission, and the faster they rotate the fainter they seem to
get.  Our papers make these effects clearer than ever, thanks to both the new
data and to work we did to build up a database of relevant measurements from
the literature. I’m really excited about the database since it’s not a one-off
effort; it’s an evolving, flexible system inspired by the architecture of the
[Open Exoplanet Catalogue](http://www.openexoplanetcatalogue.com/) (technical
paper [here](http://arxiv.org/abs/1211.7121)). It isn’t quite ready for prime
time, but I believe the system to be quite powerful and I hope it can become a
valuable, _living_ resource for the community. More on it anon.  One of the
things that the database helps us to see is that even if you look at two UCDs
that are superficially similar, their properties that are influenced by
magnetism (_e.g._, radio emission) may vary widely. This finding matches well
with results from studies using an entirely unrelated technique called
[Zeeman-Doppler
imaging](http://en.wikipedia.org/wiki/Zeeman%E2%80%93Doppler_imaging) (ZDI).
The researchers using ZDI can measure certain aspects of the UCD magnetic
fields directly, and [they have
concluded](http://dx.doi.org/10.1051/0004-6361/201220317) that these objects
can generate magnetic fields in two modes that lead to very different field
structures. These ideas are far from settled — ZDI is a complex, subtle
technique — but we’ve found them intriguing and believe that the current
observations match the paradigm well.  One of my favorite plots from the two
papers is below. The two panels show measurements of two UCD properties: X-ray
emission and magnetic field strength, with the latter being a representative
value derived from ZDI. Each panel plots these numbers as a function of
rotation (using a quantity called the [Rossby
number](http://en.wikipedia.org/wiki/Rossby_number), abbreviated “Ro”). The
shapes and colors further group the objects by mass (approximately; it’s hard
to measure masses directly).  [![X-rays and magnetic field versus
rotation.](/wp/wp-content/uploads/2013/10/rx-bv.png)](/wp/wp-
content/uploads/2013/10/rx-bv.png)  X-rays and magnetic field versus rotation.
There’s scatter, but the general trends in the two parameters (derived from
very different means) are surprisingly similar. From
[1310.6758](http://arxiv.org/abs/1310.6758).  What we find striking is that
even though the two panels show very different kinds of measurements, made
with different techniques and looking at different sets of objects, they show
similar trends: wide vertical scatter in the green (lowest-mass) objects; low
scatter and high values in the purple (medium-mass) objects; and low scatter
with a downward slope in the red (relatively high-mass) objects. This suggests
to us that the different field structures hypothesized by the ZDI people
result in tangible changes in standard observational quantities like X-ray
emission.  In our papers we go further and sketch out a physical scenario that
tries to explain the data holistically. The ZDI papers have argued that fast
rotation is correlated with field structure; we argue that this can explain
the decrease of X-rays with rotation, if the objects with low levels of X-rays
have a field structure that produces only small “short circuits” that can’t
heat gas to X-ray emitting temperatures. But if these short circuits manage to
provide a constant supply of energized electrons, that could explain the
overly bright radio emission. The other objects may produce fewer, larger
flares that can cause X-ray heating but are too infrequent to sustain the
radio-emitting electrons. (There are parallels of this idea in [studies of the
X-ray flaring properties of certain
UCDs](http://dx.doi.org/10.1051/0004-6361/200913603).)  Our papers only sketch
out this model, but I think we provide a great jumping-off point for more
detailed investigation. What I’d like to do for Paper III is do a better job
of measuring rotation; right now, we use a method that has some degeneracies
between actual rotational rate and the orientation of the object with regards
to Earth. [Some people have argued that orientation is in fact
important](http://dx.doi.org/10.1086/590360), so using different rotation
metrics could help test our model _and_ the orientation ideas. And of course,
it’s important to get more data; our “big” sample has only about 40 objects,
and we need more to really solidly investigate the trends that we think we
see.  One great part of this project is that I worked on it not only with my
boss [Edo Berger](https://www.cfa.harvard.edu/~eberger/Edo_Berger_Harvard/Main
_Page.html), but also with a fantastic summer REU student from Princeton, [Ben
Cook](https://twitter.com/bacook17). Ben’s the lead author of Paper II and he
did fantastic work on many aspects of the overall effort. It was a pleasure
working with him and I suspect he’ll do quite well in the years to come.
