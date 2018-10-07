+++
date = 2018-10-06T22:51:30-04:00
title = "Website Refresh"
+++

It’s been almost a year since my last blog post! That’s mostly because this
has been a very eventful year for me, professionally. More on that soon. But
another reason is that I’ve gotten more and more dissatisfied with WordPress.
Over the past few days I’ve finally sat down and transitioned the website to a
new system. Here it is!

<!-- more -->

This website is now powered by [Gutenberg](https://www.getgutenberg.io/), an
all-in-one static site generator written in my new favorite language
[Rust](https://www.rust-lang.org/). One great thing about this system is that
most of the text on this site is now expressed in
[Markdown](https://en.wikipedia.org/wiki/Markdown), and I can keep the whole
thing in Git version control. If there’s one thing I love, it’s putting stuff
in Git.

Gutenberg has a very straightforward architecture that makes it easy to
implement new features on the website. So I’ve gone ahead and revised the
design, changing several things that have been bothering me for a while. For
instance, I’ve tried to make the body text extremely readable — if you ask me,
almost every website has font sizes that are way too small. (I think it’s
notable that [Medium](https://medium.com/), which takes its typography really
seriously, also uses unusually large fonts.) I’ve also reduced the size of the
header since it’s just one more thing in between you and the stuff you
actually want to read.

The Markdown translation wasn’t *too* bad, but there were several moments when
I wished that [Tectonic](https://tectonic-typesetting.github.io/) was able to
emit the HTML output that I’ve been dreaming of for so long. In particular,
the equations on this site look pretty bad, and I wish I was able to define
macros using a system more powerful than Gutenberg’s “shortcodes”. Strong
motivation to push on that line of work! I really hope that one day — maybe
even soon! — I’ll have reason to translate all of this Markdown into TeX.
