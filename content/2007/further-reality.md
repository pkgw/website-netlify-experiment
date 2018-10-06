+++
date = 2007-10-30T23:35:34Z
title = "Further Reality"

[extra]
wp_rel_permalink = "/2007/10/further-reality/"
wp_shortlink = "/?p=34"
+++

Continued to look at broadband spectra data. On Friday, I did the stuff with
looking up the 3c48 model and looking at the antenna gains that I was getting
out. The gains were usually pretty flat over time, but there were some trends
and then some serious outliers that indicated that the self-cal solutions
weren’t very good.

Saturday, went observing at Lick for JohnJohn.

Monday, came in late but spent a little time looking at data from 3c84. Most
of the effort was improving the flagging situation; now I can update the list
of flags to apply to a bunch of different datasets at once. Also worked out
some handy utilities to slice through the data in different ways to look for
things that ought to be flagged — for instance, many spectra of a single
baseline over time, or overlaid spectra at the same frequency to look for RFI.
Then I stayed real late in the lab doing nothing productive at all.

Today I actually looked at the 3c84 data and made images. With the automatic
flagging, pretty much everything came through OK, although occasionally there
are baselines that cause problems for reasons that I can’t figure out. Then
came the big test of copying the self-cal solutions from the 3c48 data to the
3c84 data. That didn’t go so well. The solutions aren’t completely off, but
the amplitudes I get don’t agree well with my 3c84 model. Unfortunately my
3c84 model is something I made up from two data points from the  VLA
calibrator database, so its reliability is dubious at best. I searched around
online for a while but couldn’t find any nice published spectral models for
3c84 in the 1-10 GHz range. So maybe, just maybe, the copied self-cal
solutions actually work OK, but it looks like 3c84 has a very flat spectrum
around the ATA band and I’m getting something extremely steep, so I’m not
optimistic.

Then more time at lab. A little bit of traction on a revised, more useful
OmegaPlot. Hmm.
