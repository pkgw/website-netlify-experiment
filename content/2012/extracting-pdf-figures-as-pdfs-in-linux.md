+++
date = 2012-10-15T06:31:20Z
title = "Extracting PDF Figures as PDFs in Linux"
path = "2012/10/extracting-pdf-figures-as-pdfs-in-linux"

[extra]
wp_rel_permalink = "/2012/10/extracting-pdf-figures-as-pdfs-in-linux/"
wp_shortlink = "/?p=581"
+++

The perennial problem: you have a PDF of a paper, and you want to extract one
of its figures to show in a talk or something.

If you’re a normal person, you open it up big in your PDF viewer, take a
screenshot, and call it a day. Or your PDF reader just lets you draw a box and
save its contents.

But maybe you’re running Linux and don’t have commercial software available;
and maybe you want to make a _vector_ screenshot, not a _bitmapped_ one, so
that full detail will be maintained and you can scale the figure around.
[Evince](http://projects.gnome.org/evince/) doesn’t support draw-a-box-and-
save-it, so you’re sunk.

But you’re not! You’ll need [`xpdf`](http://www.foolabs.com/xpdf/),
[`poppler-utils`](http://poppler.freedesktop.org/), and
[`pdfcrop`](http://pdfcrop.sourceforge.net/) — all widely-available. You can
draw a box on the page in `xpdf`, and you can also set up `xpdf` to run a
command when you press a key, with the box parameters able to be substituted
into the command line. Then the `pdftocairo` utility provided by `poppler-
utils` can rerender the page to PDF while cropping to your selected box.
`pdfcrop` makes the margins nice.

You need to put [this short helper script](https://gist.github.com/3892706) in
your `$PATH`. It takes the coordinates from `xpdf`, converts them to the
system needed by `pdftocairo`, then chooses an output filename (`fig${n}.pdf`)
and makes the magic happen. There’s nothing complex about it and it can easily
be monkeyed with to fit your preferences.

Then put this line in `~/.xpdfrc`:

```
bind ctrl-e any "run(xpdf-extract-helper.sh '%f' %p %x %y %X %Y)"
```

Straightforward enough, I hope. I chose Control-E as the keybinding for
“extract”.

Now just open up your PDFs in `xpdf`, draw boxes, and hit Control-E! Here’s a
sample result … converted to a PNG so that it can render inline, so that in a
way it misses the whole point of the exercise. But there’s little PDF figure
behind it, I swear.

{% figure(src="/~peter/wp/wp-content/uploads/2012/10/mclean_2012_fig2.png-1.png") %}
McLean et al (2012 ApJ 746 23), fig 2. I assert without proof that I have a PDF version of this image.
{% end %}
