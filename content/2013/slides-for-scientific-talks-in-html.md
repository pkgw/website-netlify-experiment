+++
date = 2013-09-19T18:48:43Z
title = "Slides for scientific talks in HTML"

[extra]
wp_rel_permalink = "/2013/09/slides-for-scientific-talks-in-html/"
wp_shortlink = "/?p=771"
+++

As a Linux user, I’ve long been making slides for my talks in
[LibreOffice Impress](http://www.libreoffice.org/features/impress/) (formerly
OpenOffice Impress), the Free Software clone of PowerPoint. I don’t envy
_anyone_ who’s trying to maintain compatibility with Microsoft Office
products, but frankly Impress has been slow and frustrating and buggy, and my
use of it has been grudging at best.

Recently, however, I encountered an unusually wonderful bug where graphics in
EPS format showed up everywhere _except_ on the screen for the actual
presentation — I confidently started my talk and moved to my first science
slide, only to find an empty black expanse, which most of my subsequent slides
were as well. Everything was fine on my laptop. And I said to myself: _effffff
this_.

Today I happen to be at [Bucknell University](https://www.bucknell.edu/),
where I just gave a colloquium to an audience of mostly physics
undergraduates. I hadn’t given a talk aimed at this kind of audience before,
so I had to make a bunch of new slides anyway. So, early last week, I took the
plunge and tried to see if I could prepare my slides using HTML and show them
in Firefox.

Why HTML? Well, I really like the idea of having my slides being stored in
text format, so I can version-control them, edit quickly, and so on. And
crucially, web browsers are now sophisticated enough that you can make
great-looking slides in them — I don’t think this was true five years ago. It
also seems _really_ cool to have the option of embedding YouTube videos, Flash
animations, interactive JavaScript demos, and all that kind of stuff. I didn’t
do much of that in this talk, but I did put in a bunch of movies, which I’d
never dared to do with Impress.

The experiment was a resounding success. I found a framework,
[reveal.js](http://lab.hakim.se/reveal-js/), that made it easy to prepare the
slides and supported a few features that are pretty vital for scientific
talks:

- Ability to make a PDF out of the talk, in case disaster strikes or you’re
  not allowed to use your own computer.

- Ability to use PDF graphics in slides (straightforwardly done with Mozilla’s
  [pdf.js](http://mozilla.github.io/pdf.js/)).

- A “presenter console” mode with offscreen speaker notes.

- As a bonus, easy embedding of relatively
  nice-looking equations with [MathJax](http://www.mathjax.org/).

It took some time to get the appearance to be how I wanted and to figure out
how best to construct slide layouts, but all told it wasn’t too bad. I _loved_
being able to edit and rearrange my slides efficiently, and I’m very happy
with the aesthetic appearance of the final product.

[I put the presentation source code on GitHub](https://github.com/pkgw/htmltalk)
so you can see how I did it. I did devise a few new tricks (such as working
out how to embed PDFs), but most of the work was just using the stock
`reveal.js` toolkit and tweaking the styling.
[Here’s a live, online version of the talk](https://www.cfa.harvard.edu/~pwilliam/htmltalk/)
so you can see how it looks.

I wrote up some more detailed notes on the
[repository README](https://github.com/pkgw/htmltalk#readme). To be honest,
this approach probably isn’t right for most astronomers — most astronomers
have Mac laptops with Keynote, which is a lot better than Impress. And I
needed to draw on a lot of technical background in order for the slide
construction to feel “easy”. But once I got the template set up, it was quick
and fun to make slides, and now here’s a template that you can use too!

Big thanks to [Hakim El Hattab](http://hakim.se/) for making and publishing
`reveal.js`, as well as to the authors of the various CSS/JavaScript tools I
used. It was kind of incredible how easy it was to achieve some fancy,
beautiful effects.
