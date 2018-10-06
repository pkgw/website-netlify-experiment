+++
date = 2007-10-25T20:01:35Z
title = "Real Work!"
path = "2007/10/real-work"

[extra]
wp_rel_permalink = "/2007/10/real-work/"
wp_shortlink = "/?p=33"
+++

Today I actually looked at my broadband spectra data for the first time in
what feels like forever! Got a fair amount done: I generated images of 3c48 in
our seven single-pol correlator slices at several sets of frequencies. The
difficulty there was mostly flagging the data. Fortunately it seems like the
visibilities that need to be flagged can be broken down into two orthogonal
cases: something that’s bad at every frequency in a given slice (i.e., bad
antennas or baselines), or something that’s bad in every slice at a given
frequency (RFI). I worked out a little system that allows me to flag things
and check the results pretty quickly and I was able to work through several
data sets with a pretty consistently high mojo, where mojo = (speed) *
(confidence in results).

So far, all I have is a bunch of images of point sources of varying quality.
Tomorrow, I’ll look up a model of 3c48’s emission and actually scale my
results by the correct amount; then I’ll look at the antenna gains that I’m
finding and see how they vary from one frequency to another. I believe they
should be more-or-less constant with some kind of linear trend. There are
probably a lot of ways to spend time transferring the self-cal results from
one dataset to another to try and improve the results. Once I look at and
think about the gains, I may experiment a bit there.

If things go really fast, I might even be able to reduce the data for another
source and see how the gains compare from one source to another. Unfortunately
Miriad doesn’t provide great tools for manipulating and visualizing gain
information, but I think I have the tools to put together the … more tools …
that I need without too much difficulty.
