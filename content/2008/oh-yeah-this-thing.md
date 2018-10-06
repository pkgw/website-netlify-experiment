+++
date = 2008-05-26T18:35:03Z
title = "Oh Yeah, This Thing"
path = "2008/05/oh-yeah-this-thing"

[extra]
wp_rel_permalink = "/2008/05/oh-yeah-this-thing/"
wp_shortlink = "/?p=70"
+++

Seem to have accidentally taken a long break from this. Not sure why, as I’ve
been working away for the past few weeks. I have been pushing a few very
different projects, though, and have had trouble getting a good groove going
on any of them. I feel like I’ve been learning things, but not accomplishing
all that much concretely, and it’s a bit less motivating to write about
things.

Anyway. My various projects have all been related to the usual things:
understanding the ATA systems better and trying to figure out what I need to
do to get my data to work. I think I’ll describe them later and in this post
finally get around to describing flagging.

Flagging isn’t that complicated, actually. It’s the process of taking the data
recorded by the ATA and manually removing the bits that are bad. Well, the way
the data are stored, the bad parts aren’t removed, they’re just marked as bad,
and the tools ignore them subsequently.

The general process of eliminating bad data is common to pretty much all
experimental science but the flagging of interferometer data is a bit of a
special process, due to a few factors:

- It takes a lot of steps to generate data from the ATA (and radio arrays in
  general), so there are a lot of places for noises and errors to creep in.
- The UV data you get out of an interferometer are pretty complicated: you get
  points inhabiting a multidimensional space of time, baseline, polarization,
  frequency, and complex value. The data are hard to visualize, and so it’s
  hard to get a quick summary of a dataset and pick out by eye what needs
  work.
- Generally, flagging is a trial-and-error process, in which dubious-looking
  data are removed, the data are reprocessed, and it’s checked whether the
  results look better or worse. As above, this is necessary because the raw
  data are so hard to visualize directly and are so far from the final
  product.
- Finally, flagging ATA data is hard since we generate so much of it: a
  night’s worth will usually be tens of gigabytes, composed of a stream of
  hundreds of datapoints coming every few seconds over the course of eight
  hours.

There are many things that ought to be flagged: misbehaving antennas,
temporary interference, bad digital hardware, satellite emissions, and lots of
datapoints that are clearly bad for unknown reasons. Some of these will be in
effect over the entire course of the observation; some will last only for a
few seconds. Some affect a vast majority of the data points, some only a
random few. Some repeat, some show up once and never again.

All that being said, once again, by “flagging” we just mean the general
process of getting rid of the junk. When I say that I’m flagging things, I
mean that I’m working through a little checklist that I’ve worked out to check
for various common types of problems and double-check that everything left
over looks good. Unfortunately, while there are common kinds of corruption you
see, it’s very hard to automate the removal of most of them, so flagging is
something that one must spend a lot of time doing by hand. Unfortunately.
