+++
date = 2007-12-01T20:18:51Z
title = "A Little Flagging"
path = "2007/12/a-little-flagging"

[extra]
wp_rel_permalink = "/2007/12/a-little-flagging/"
wp_shortlink = "/?p=48"
+++

Spent most of yesterday taking care of miscellaneous errands, so not so much
accomplished. But did get some very promising work done with the flagging. I
cooked up a routine that automatically identifies RFI-affected spectral
regions in one chunk of data that I’m looking at. I worry that it won’t
generalize very well, but the basic technique is one that will at least
sometimes be useful.

Very soon I’ll need to start working on the infrastructure to do automatic
flagging based on multiple scans through multiple datasets. This is a little
tricky since we may be talking tens of gigabytes to zip through and process,
so there need to be ways to accumulate information then act on it later. Got
some initial work done on this front but will need to write a lot more code to
see if the approach is any good.
