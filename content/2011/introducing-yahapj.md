+++
date = 2011-12-01T00:40:05Z
title = "Introducing: yahapj"

[extra]
wp_rel_permalink = "/2011/12/introducing-yahapj/"
wp_shortlink = "/?p=479"
+++

Ready for some esoteric software?

Lots of astronomers write articles for submission to
[The Astrophysical Journal](http://iopscience.iop.org/0004-637X) (“ApJ”) using
[LaTeX](http://www.latex-project.org/) for manuscript preparation and the
companion [BibTeX](http://www.bibtex.org/) for automated bibliography
processing. One uses a “style file” to tell BibTeX how to format the
bibliography according to ApJ specifications. The
[American Astronomical Society](http://aas.org/) and
[NASA Astrophysics Data Systems](http://adsabs.harvard.edu/) provide such a
style file, currently found
[here](http://ads.harvard.edu/pubs/bibtex/astronat/apj/apj.bst), but it has a
few shortcomings:

- References to [ArXiV](http://arxiv.org/) preprints don’t have their
  identifiers displayed.

- Entries with [DOI](http://www.doi.org/) information don’t use this to link
  to the referenced articles.

- Some BibTeX entries end their page numbers with a plus sign, and these get
  propagated into the bibliography and look bad.

(OK, the second two problems are pretty much cosmetic. The first one is
significant, though.) Various people have fixed some of these problems, but
there’s no canonical source of the ApJ style file, so things get out of sync.
(For instance, AAS and NASA ADS currently post differing versions of the style
file.)

Well, you can see where this is going. I’ve created a hacked version of the
style file called `yahapj.bst` — “Yet Another (h)ApJ BibTeX Style”. It fixes
the above problems, and I’ve attempted to solve the splintering issue by
managing revisions on [GitHub](https://github.com/), here:
[github.com/pkgw/yahapj](https://github.com/pkgw/yahapj). The key benefit is
that if people share their changes by cloning the Git repository and making
commits, it will always be possible to compare the lineages of different
versions of the file and merge them safely. Overkill? Perhaps. But it’s the
correct solution.

To summarize, why should you use yahapj?

- Attractive, ApJ-compliant bibliographies with embedded links to digital
  articles and preprints whenever possible.

- It’s easy to check that you’re using the latest, greatest version, and as
  easy to hack the file as you can get. (Which isn’t super-easy given BibTeX’s
  bizarre style language, but that’s another issue.)

I’ve even got a screenshot!

{% figure(src="https://newton.cx/~peter/wp/wp-content/uploads/2011/12/yahapj.png") %}
yahapj in action!
{% end %}

The blue parts are links in the PDF file. If you’re about to say something
about journal abbreviations, I know, and it’s beyond the control of yahapj.
