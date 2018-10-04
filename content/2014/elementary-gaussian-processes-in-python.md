+++
date = 2014-03-29T13:30:27Z
title = "Elementary Gaussian Processes in Python"

[extra]
wp_rel_permalink = "/2014/03/elementary-gaussian-processes-in-python/"
wp_shortlink = "/?p=854"
+++

Gaussian processes are [so hot right now](https://speakerdeck.com/dfm/an-
astronomers-introduction-to-gaussian-processes), but I haven’t seen examples
of the very basic computations you do when you’re “using Gaussian processes”.
There are tons of packages that do these computations for you — [scikit-
learn](http://scikit-learn.org/stable/),
[GPy](https://github.com/SheffieldML/GPy),
[pygp](https://pypi.python.org/pypi/pygp) —but I wanted to work through some
examples using, and showing, the basic linear algebra involved. Below is what
I came up with, as incarnated in an [IPython
notebook](http://ipython.org/notebook.html) showing a few simple analyses.
This post is also a pilot for embedding IPython notebooks on this blog.
Overall it was pretty straightforward, though I had to insert a few small
tweaks to get the layout to work right — definitely worth the effort, though!
I haven’t really used an IPython notebook before but I gotta say it worked
really well here. I generally prefer the console for getting work done, but
it’s a really nice format for pedagogy.
