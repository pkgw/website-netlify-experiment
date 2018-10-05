+++
date = 2012-05-02T20:04:30Z
title = "Quick Note on Compiling CASA"

[extra]
wp_rel_permalink = "/2012/05/quick-note-on-compiling-casa/"
wp_shortlink = "/?p=545"
+++

Today I started compiling my own version of [CASA](http://casa.nrao.edu/) to
track down and destroy a bug that’s stalling my data analysis. (It’s in what
should be a simple and robust subsystem, which is depressing, but that’s a
whole other story.)

Any normal person will find building CASA to be an enormous challenge, but
fortunately I have a ton of experience in this area and although things are
incredibly tedious, they’ve been fairly tractable.

Excluding one huge pitfall that I fell into.

CASA requires a software package called `ccmtools`. If you Google it, you find
a stale SourceForge page for the project. **Do not go there**. If you read
down the Google results, you find
[Building CCMTools as required by CASA](http://www.mrao.cam.ac.uk/~bn204/alma/sweng/ccmtools.html).
**Do not go there**. These resources reference an older version of `ccmtools`
which uses _the worst build system I have ever seen_ and doesn’t even work
anyway. I found a bit of gruesome fascination in the intersection of idiotic
design, worthless documentation, and grossly incompatible versions, but that
was all below a layer of bottomless, unfathomable rage. Don’t go there.

Instead, go to
[Compiling casapy from source in Ubuntu](https://safe.nrao.edu/wiki/bin/view/Software/CasaDevUbuntu)
and follow the tip: there’s now a
[CASA fork of ccmtools](https://svn.cv.nrao.edu/view/ccmtools/trunk/) which
builds in a much saner (though still somewhat weird) way. For the love of all
that is good, use it. I’m going to give it some more links so that hopefully
Google reorders its results. Look,
[ccmtools for CASA](https://svn.cv.nrao.edu/view/ccmtools/trunk/)! If you want
to compile [ccmtools](https://svn.cv.nrao.edu/view/ccmtools/trunk/), use the
[NRAO version of ccmtools](https://svn.cv.nrao.edu/view/ccmtools/trunk/)!

As I mentioned, the rest of the CASA build process is still a huge pain, and
would be impossible for the average person, which is too bad, but (so far?)
this has been by far the worst part.

Finally, to the guy who wrote Confix: please do not ever write code again.
