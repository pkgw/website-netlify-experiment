+++
date = 2013-05-30T00:15:25Z
title = "Numbered reverse-chronological CV listings with BibTeX"

[extra]
wp_rel_permalink = "/2013/05/numbered-reverse-chronological-cv-listings-with-bibtex/"
wp_shortlink = "/?p=744"
+++

Prompted by a [yahapj](/2011/12/introducing-yahapj/ "Introducing:
yahapj")\-related question from [Máté
Ádámkovics](http://astro.berkeley.edu/~madamkov/), I spent a little bit of
time this evening figuring out how to get a “fancy” publication listing from
BibTeX, where the papers are listed like:

```
[3] Some guy and me, 2013
[2] Me and someone else, 2010
[1] My first paper, 10,000 BC
```

I found a fragile way to make it work:

1. Make a copy of your preferred BibTeX style file and modify it to use the
   code [in this StackExchange answer](http://tex.stackexchange.com/a/33332)
   to reverse-sort your bibliography by year and month. (If you only know the
   base name of your style, you can find it with the command `kpsewhich
   basename.bst`)

2. If necessary, also modify the style file to only output `\bibitem{key}
   text` rather than `\bibitem[abbrev]{key} text`, since our hack can’t handle
   the latter.

3. Add the scary preamble from
   [this StackExchange answer](http://tex.stackexchange.com/a/75613) to your
   TeX file to reverse the bibliography list counters.

4. Put the preamble after other `\usepackage` commands and use as few of them
   as possible, since they seem to break the magic pretty easily.

5. Stick a `\nocite{*}` command in your TeX file somewhere. This causes BibTeX
   to emit a record for every item in your `.bib` file. (I’m presuming that
   you have a `mypubs.bib` file containing all of your publications and only
   your publications.)

Not exactly easy. But if there’s call for it, I’ll polish up the changes and
add them to [the yahapj repository](https://github.com/pkgw/yahapj/) with an
example `cv.tex` for reference.
