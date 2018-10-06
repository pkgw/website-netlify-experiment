+++
date = 2009-01-21T16:57:50Z
title = "For Future Reference"
path = "2009/01/for-future-reference"

[extra]
wp_rel_permalink = "/2009/01/for-future-reference/"
wp_shortlink = "/?p=99"
+++

To get dual-head output on a recent Intel integrated graphics card, such as
the 965 GM inside my Lenovo T-61 laptop, when running Fedora 10, only one
relatively non-intuitive step is needed. The virtual desktop size must first
be increased inside `xorg.conf` so that both screens can fit inside the single X
framebuffer:

```
Section "Screen"
   ...
   SubSection "Display"
      ...
      Virtual 3072 1680
   EndSubSection
EndSection
```

Once this is done, you can plug in a display (say, a projector), go to the
“Resolution” preferences applet, and enable the new display at a reasonable
resolution. F10’s version of [OpenOffice.org](https://openoffice.org/) even
has a fancy two-screen presentation mode that shows a countdown timer, the
next slide, etc.

Answer discovered on
[this documentation page](http://intellinuxgraphics.org/dualhead.html).
