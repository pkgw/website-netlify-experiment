+++
date = 2008-03-31T21:35:20Z
title = "FX64 Work"

[extra]
wp_rel_permalink = "/2008/03/fx64-work/"
wp_shortlink = "/?p=61"
+++

Spent today working on reducing some sample FX64 data. Got a rough recipe
together, and it seems to yield pretty good results. Writing the steps down
makes a big difference in thinking about how to do things and making sure that
you do a thorough job of looking at things.  The next step, I think, is to
work with some more complicated data. Right now I’m just reducing a big
blazing calibrator image, which doesn’t stress things much. I’d be interested
in extending it to observations of more interesting sources. I think the
extension will be straightforward, but it’d be good to check how things work.
That sort of work isn’t too relevant to my project, though, so I may not spend
too much time on it.  Another thing that I could do is unify my code a bit
better. I have a lot of modules doing very similar things but with mutually
incompatible implementations. Unfortunately, it’s difficult to get things
talking to each other while also being flexible enough so that the different
bits can do what they need to do. I have some vague ideas that I think are
sensible, though, so I’d like to imagine that I can make my various modules at
least play together a bit better. On the other hand, it’s definitely not a
good idea to get too stuck on beautifying the framework, since that activity
can consume unbounded amounts of time.  Overall, I do have a sense that the
necessary tools are coming together. It’s never going to be perfect, but I can
obtain the most of the numbers I want and visualize them how I want. Combine
the ability to do that with a good recipe for reducing the data (which I am
actively developing) and you’re about as good as you can ask for.
