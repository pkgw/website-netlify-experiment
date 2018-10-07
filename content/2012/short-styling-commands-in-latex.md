+++
date = 2012-02-16T16:30:00Z
title = "Short Styling Commands in LaTeX"
path = "2012/02/short-styling-commands-in-latex"

[extra]
wp_rel_permalink = "/2012/02/short-styling-commands-in-latex/"
wp_shortlink = "/?p=501"
+++

In various LaTeX files I know that I’ve seen magic performed so that, for
instance, code “`typed |like| this`” gets rendered as “typed **like** this”.
It took me a lot of Googling, but I finally found a way to do this. The short
version is:

```tex
\catcode`\|=\active
\protected\def|#1|{\textsf{#1}}
```

This example sets up the pipe symbol as the magic delimiter and uses the
`\textsf` command to render pipe-enclosed text in a sans-serif font. Note that
this **will** break vertical lines in table format specifications (e.g.),
although pipes do seem to be the standard choice for the magic character.
(Primary credit to [StackExchange](http://tex.stackexchange.com/q/40513).)

If you want to do this to render the enclosed characters in “verbatim” format,
the [shortvrb](https://ctan.org/pkg/shortvrb?lang=en) package seems to take
care of things.

According to
[this StackExchange answer](http://tex.stackexchange.com/a/40687), the above
definition falls down in some corner cases (“will not work if you want
verbatim text mixed with your emphasized text”) but they don’t sound like
cases I care about.

Journals probably won’t be happy if you have this kind of stuff in your LaTeX
files but I haven’t tried submitting anything containing commands like these.
