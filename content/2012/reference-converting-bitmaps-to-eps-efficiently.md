+++
date = 2012-03-01T10:04:20Z
title = "Reference: Converting bitmaps to EPS efficiently"

[extra]
wp_rel_permalink = "/2012/03/reference-converting-bitmaps-to-eps-efficiently/"
wp_shortlink = "/?p=512"
+++

Yet another entry in a [surprisingly](/?p=469) [long](/?p=352) series of
reference posts about converting image formats. Sometimes you have a bitmap
plot that needs to be converted to EPS for submission to a journal. My go-to
command is `convert foo.png foo.eps` but this can give bad results.  For a
large PNG file, the best approach using standard tools that I’ve discovered is
to use the NetPBM programs:  pngtopnm figure.png |pnmtops -equalpixels -scale
0.24 -psfilter \\    -flate -noturn -ascii85 -nocenter - >figure.eps
Annoyingly all of these options seem to be necessary to give useful output.
The scale factor is the number of inches per 72 pixels; 0.24 gives you about
300 DPI.  The `pnmtops` documentation says that the `-flate` option (which
turns on compression and can be a huge deal for large images) sometimes
produces busted output. There’s also an `-rle` option that will be less
efficient (especially for bitmaps that don’t contain long stretches of single
colors). The documentation also references a program called
[`bmeps`](http://dktools.sourceforge.net/bmeps.html) that is claimed to do a
better job of this kind of conversion. The same seems to be said of
[`sam2p`](http://code.google.com/p/sam2p/), but one of the benefits of the
above command is that the NetPBM tools are installed on most Linux machines.
When all of these options are working, I can generate a good EPS that’s only
15% larger (on-disk) than the original PNG, which is pretty cool.
