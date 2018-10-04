+++
date = 2007-08-30T23:49:31Z
title = "Aperture Photometry: Not So Simple"

[extra]
wp_rel_permalink = "/2007/08/aperture-photometry-not-so-simple/"
wp_shortlink = "/?p=8"
+++

I think I did a fairly good job of restraining myself and spent a minimal
amount of time on overengineered plotting infrastructure today. I needed to
write some code to help me see what I was doing with the HAT data, but I
didn’t end up writing too much of it. I also found a SciPy implementation of
2D Gaussian fitting, which saved me some potential headaches.  I used the
Gaussian fitter and some coordinate display code to get good positions for the
stars of interest in the HAT data. I spent some time fiddling with that until
it occurred to me that, you know, part of fitting a 2D Gaussian is deriving an
amplitude, which could be kind of useful for photometry. Unfortunately, this
kind of boneheaded PSF fitting wasn’t very effective. I’m not 100% sure that I
was doing things correctly, but whatever I was doing yielded some really poor
results. Spent some time seeing if I was just slicing the data the wrong way,
but that doesn’t seem to have been the case.  I then moved from doing lame,
home-brewed PSF fitting to lame, home-brewed aperture photometry. It wasn’t
hard to write some quick routines to add up the pixels inside an annulus;
then, doing that around the stars of interest and the sky patches, voila,
instant aperture photometry. I think. Unfortunately, this also yielded sub-
spectacular results. As with the PSF fitting, I wrote all the code without
really checking how things are supposed to be done, which probably has
something to do with the fact that my results are horrible. (I checked, and
the data from the night that I’m using caught nearly a complete  transit, and
the lightcurve in the HAT-P-1b paper has really good precision, so I can’t
just blame the data. In retrospect, I should have checked that this night was
good before starting working on the reduction routines. I seem to be really
good at not doing things that I know to be good ideas.)  At the end of the
night, I decided to stop being dumb and found myself a copy of the _Handbook
of CCD Astronomy_. The flimsy excuse I have for not going to it _before_
writing code is that I couldn’t think of where to get one; but unsurprisingly
there are three copies in the undergraduate lab. I’ve only started reading a
few sections, but I hear that the book is good, and at the very, very least
it’ll let me check that I’m actually correctly remembering how this relative
photometry stuff is supposed to be done. (Or I assume it will.)  But I really
need to get better at researching previous work before diving in and doing
something myself. Cough, cough, plotting and numerical code. Seriously, I
realize that the way I go about things right now is not smart, and yet I keep
on doing it. It’s weird how blatantly irrational people can be.  (_Years-later
update:_ of course, the Greeks have a word for this phenomenon:
[akrasia](http://en.wikipedia.org/wiki/Akrasia).)
