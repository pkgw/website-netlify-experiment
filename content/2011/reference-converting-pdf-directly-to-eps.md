+++
date = 2011-10-20T10:03:23Z
title = "Reference: Converting PDF Directly to EPS"

[extra]
wp_rel_permalink = "/2011/10/reference-converting-pdf-directly-to-eps/"
wp_shortlink = "/?p=469"
+++

Simple: `pdftops -eps figure.pdf figure.eps`, using a program from the
`poppler-tools` package. This deals with white space on the edge of the
bounding box much better than `pdf2ps`, and seems to deal with text better
too.
