+++
date = 2010-09-05T16:18:34Z
title = "Reference: PostScript to PNG Conversion"

[extra]
wp_rel_permalink = "/2010/09/reference-postscript-to-png-conversion/"
wp_shortlink = "/?p=352"
+++

I’ve usually used the ImageMagick program `convert` to get a bitmap out of
PostScript files, but it can be hard to drive and the useful documentation is
hidden among hundreds of commandline options to apply weird visual effects.
The `latex2html` program `pstoimg` seems to do well when given a few key
arguments:  pstoimg -antialias -density 300 -type png -out foo.png foo.ps
Here “300” is the DPI at which to generate the image, and the `-antialias` is
important for good results. It looks like a `-geometry` argument may be
important for EPS files if they have bounding boxes that aren’t what you want.
**Update:** One thing to watch out for is that `pstoimg` doesn’t handle paths
with spaces in them correctly. Just work around that.
