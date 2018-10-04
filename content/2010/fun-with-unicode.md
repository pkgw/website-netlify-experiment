+++
date = 2010-10-11T21:21:46Z
title = "Fun With Unicode"

[extra]
wp_rel_permalink = "/2010/10/fun-with-unicode/"
wp_shortlink = "/?p=362"
+++

A common annoyance when typing science-y things is that you often want to use
symbols that aren’t available on standard keyboards: Greek letters, math
symbols like ±, or em-dashes (if you’re the kind of person that thinks em-
dashes are cool). It turns out that nowadays, you can type all of these
symbols and more with relative ease and good confidence that other people will
be able to see them, thanks to the [Unicode](http://unicode.org/) standards.
By now, not only is basically everything that works with text on a computer
Unicode-enabled, but people have gotten their act together regarding entering
Unicode characters if they’re not on your keyboard. I’ve found two mechanisms
to be helpful for this.  The first is a “[compose
key](http://en.wikipedia.org/wiki/Compose_key)“, which you can set up in your
keyboard settings. This is a physical key on the keyboard that you tell the OS
to interpret specially — I like to use the “context menu” key that lives near
the right control key. The compose key is a “do what I want” kind of feature
best illustrated by example:  *   Typing “<compose> a <apostrophe>” yields á *
“<compose> + -” yields ± *   “<compose> ^ 2” yields ² *   “<compose> o o”
yields ° *   “<compose> <dash> <dash> <dash>”  yields — (an em-dash) *
“<compose> <dash> <dash> .” yields – (an en-dash) *   “<compose> <dash> >”
yields →  Every graphical application that I’ve tried supports input this way.
[This table](http://www.hermit.org/Linux/ComposeKeys.html) lists some of the
many special characters you can construct with a compose key.  Some useful
special characters aren’t supported by the compose key, though, including most
of the Greek letters. It turns out that most programs that allow text input
have a way for entering an arbitrary Unicode character if you know its Unicode
representation. These representations are four-character hexadecimal codes and
are usually written with a prefix of “U+”. For instance, the code for the
Greek letter alpha is U+03B1. I’ve only needed to figure out two ways to use
this information:  *   For the graphical applications I use, I can hit
Control-Shift-u, type 03B1, then hit space to insert α. (This may be specific
to [GTK](http://gtk.org/)\-based applications but seems to be a common
standard.) *   In Emacs, hit “<Control>-x 8 <return>” and type in 03B1. This
is equivalent to running the ELisp function ucs-insert.  Obviously, we’ve all
got better things to do than memorize Unicode codepoint values, but it’s the
kind of information that goes well on a Post-It note on one’s monitor. The
Greek letters in particular go in sequence, so β is U+03B2, γ is U+03B3,
_etc._, so one can guess-and-check a little bit. Another one that I like to
use is U+2022, the middle bullet: •.  With all of these skills in hand, one
can go from typing “alpha = 0.5 +- 0.1 (reduced chi-squared = 1.2)” to “α =
0.5 ± 0.1 (reduced χ² = 1.2)”. Hooray!  **Technical note.** You can embed
Unicode characters into string constants in Python programs if you give the
interpreter a hint that your program is UTF8-encoded. This can be done by
adding a bit to an Emacs modeline to make it read “-\*- mode: python; coding:
utf-8 -\*-“. More info in [PEP263](http://www.python.org/dev/peps/pep-0263/).
**Technical note #2.** It turns out that the compose key definitions live in
the file /usr/share/X11/locale/en\_US.UTF-8/Compose, for my current setup at
least.
