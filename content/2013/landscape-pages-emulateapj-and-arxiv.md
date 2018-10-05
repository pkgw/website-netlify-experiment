+++
date = 2013-10-24T11:19:34Z
title = "Landscape pages, emulateapj, and arxiv"

[extra]
wp_rel_permalink = "/2013/10/landscape-pages-emulateapj-and-arxiv/"
wp_shortlink = "/?p=801"
+++

The past couple of times that I’ve put up a paper on
[arxiv.org](http://arxiv.org/), I’ve had trouble with pages rotated to
landscape mode. Here’s a quick note on what the issue is.

I’ve been using the `pdflscape` package to get landscape-oriented pages. It
seems to be the standard LaTeX solution for this kind of thing. There’s also
an `lscape` package; they’re almost the same, but if you’re using `pdflatex`
the former inserts some magic to get the relevant page of the output file
automatically turned when viewed on your computer.

The problem is that `lscape` and `pdflscape` have some kind of problem with
the `revtex4-1` document class, and `revtex4-1` is what drives `emulateapj`
under the hood. When you use them, the content on every page in the document
is rotated in a bad-news kind of way. It took me a while to figure this out
because I had only `revtex4` installed on my laptop; `emulateapj` can work
with either, and the older version doesn’t have the issue.
[arxiv.org](http://arxiv.org/) does have `revtex4-1,` so the problem would
seem to only appear for Arxiv submission.

Recent versions of `emulateapj` have a `[revtex4]` option to force use of the
older version of the package, which should make this go away. I don’t know if
Arxiv’s version of `emulateapj` is new enough to support this.

Alternatively,
`revtex` comes with its own environment for rotating pages, `turnpage.` You
can use this instead. Here’s an example of rotating a wide single-page
`deluxetable` at the end of a document:

```tex
...
\clearpage
\begin{turnpage}
\begin{deluxetable}
...
\end{deluxetable}
\end{turnpage}
\clearpage
\global\pdfpageattr\expandafter{\the\pdfpageattr/Rotate 90}
\end{document}
```

The `\pdfpageattr` line gets the magic PDF page rotation to happen. Obviously,
this assumes that `pdflatex` is being used. I do _not_ know if this works with
multipage tables. More annoyingly, you still seem to be forced to place the
table at the end of the document, which is lame. At least, I don’t know how to
get the `deluxetable` onto its own page without seriously messing with the
flow of the surrounding document. (From what I read, the `\pdfpageattr`
command lasts until you change it, so if you somehow got a rotated table into
the middle of the document, you’d also need to figure out how clear the PDF
page rotation afterward.)
