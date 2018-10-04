+++
date = 2009-01-21T16:57:50Z
title = "For Future Reference"

[extra]
wp_rel_permalink = "/2009/01/for-future-reference/"
wp_shortlink = "/?p=99"
+++

To get dual-head output on a recent Intel integrated graphics card, such as
the 965 GM inside my Lenovo T-61 laptop, when running Fedora 10, only one
relatively non-intuitive step is needed. The virtual desktop size must first
be increased inside xorg.conf so that both screens can fit inside the single X
framebuffer:  Section "Screen"    ...    SubSection "Display"       ...
Virtual 3072 1680    EndSubSection EndSection
