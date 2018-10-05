+++
date = 2011-12-05T16:36:25Z
title = "Reference: MIRIAD and Fortran 90"

[extra]
wp_rel_permalink = "/2011/12/reference-miriad-and-fortran-90/"
wp_shortlink = "/?p=484"
+++

A note-to-self for reference.

I tried to convert MIRIAD to use FC instead of F77 but it turns out to
basically be a massive undertaking. As far as I can tell there’s no way to
convince Automake to treat `.f` or `.for` files as Fortran 90, not Fortran 77.
(Search for .f90 in `/usr/bin/automake`, e.g.)

There’s a potential win here because the .for files can be compiled directly
by gfortran without needing preprocessing by ratty, at least in the cases I’ve
tried. It’d be very nice to skip the ratty circumlocutions.

Also note that wcslib and linpack come with `.f` files. If there’s a trick to
get automake to think of `.for` files as Fortran 90, if it can’t also be
applied to `.f` files, we’ll still need to use F77 to build those libraries.
(The same consideration applies to pgplot too, but it has its own configure
script.)
