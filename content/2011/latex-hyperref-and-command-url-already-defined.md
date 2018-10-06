+++
date = 2011-06-29T11:03:34Z
title = "Reference: LaTeX, hyperref, and “Command \\url already defined.”"
path = "2011/06/latex-hyperref-and-command-url-already-defined"

[extra]
wp_rel_permalink = "/2011/06/latex-hyperref-and-command-url-already-defined/"
wp_shortlink = "/?p=413"
+++

Another random computer fix. I was trying to compile a document with
`pdflatex`, and was getting:

```
LaTeX Error: Command \url already defined.
```

My document used the `hyperref` package, and disabling this did make the
problem go away. But I could compile the document on another machine without
problems.

It turned out that the culprit was the `latex2html` package. The `hyperref`
package requires a package called `url.sty`, which normally has some special
hooks that are invoked when `hyperref` (and perhaps `pdflatex`) are active.
However, `latex2html` comes with an old version of `url.sty` that doesn’t have
these hooks, and on my machine LaTeX prefers the version that comes with
`latexhtml` (in the `tex/latex/html/` subdirectory of the `texmf` tree) to the
usual version (in `tex/latex/ltxmisc/`).

Uninstalling `latex2html` solved the problem. Of course, now I don’t have
`latex2html`, but I don’t need it at the moment.
