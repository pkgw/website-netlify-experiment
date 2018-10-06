+++
date = 2007-11-13T22:06:26Z
title = "Spectrum Tweaking"
path = "2007/11/spectrum-tweaking"

[extra]
wp_rel_permalink = "/2007/11/spectrum-tweaking/"
wp_shortlink = "/?p=43"
+++

Star Formation lecture this morning, then working on seeing if we could throw
together better broadband spectrum results. The high-frequency performance
wasn’t too great (that is, the fluxes we got for 3c138 didn’t match the model
very well at all) and Geoff and I wanted to see if we could find a better
technique.

There were definitely some slices with poor performance at high frequencies,
so Geoff suggested that I consider only the best-performing slice.
Unfortunately, doing this led to images that were clearly crap. We spent a
long time trying to figure out what was going on, since the inversion process
is basically linear, so separating out the OK combined image by slice should
lead to several also-OK images, not several horrible ones. After a lot of
head-scratching, Geoff realized that the raw images weren’t too bad, but that
the clean algorithm was failing horribly because the individual slices had
really awful beams, making the restored images look awful.

This suggested a better approach: use a task called ‘uvfit’ to do the
point-source fitting without inverting at all, avoiding the beam issues
altogether. It wasn’t too hard to try this out, and it indeed seems to give
much better results. The fluxes still miss the model values, but not much
worse than they do down at ~1.5 GHz. And per-slice analysis works OK, so I can
cherrypick the best slices to get the nicest looking results.

Lab in the evening. Made a few important fixes to OmegaPlot. Much happier with
the revamped API. I think I’m on the verge of installing the new version over
the old version that I’ve been putting up with; I think they’re about at
feature-parity now, and it’s so much easier to actually use the new version. A
few more nontrivial-but-manageable improvements and I think it’ll be really
nice.
