+++
date = 2009-08-28T15:53:34Z
title = "Parallel Computing Bootcamp"
path = "2009/08/parallel-computing-bootcamp"

[extra]
wp_rel_permalink = "/2009/08/parallel-computing-bootcamp/"
wp_shortlink = "/?p=156"
+++

Last week I attended the
[2009 Short Course on Parallel Programming](http://parlab.eecs.berkeley.edu/2009bootcamp),
a boot camp put on by the Berkeley EE/CS
[Parallel Computing Lab](http://parlab.eecs.berkeley.edu/). The “parallel” in
the names refers to computers in which you have several independent processors
that work on computational problems cooperatively and simultaneously. Pretty
much everyone agrees that this is the future of computing, since chip
manufacturers have just about maxed out the raw computing power of single
processors. To satisfy the never-ending lust for higher-performing computers,
then, they’re all racing to find ways to pack more processing cores into a
smaller area with faster communication between them. Most people expect that
in the not-too- distant future, typical desktop computers will contain
something like 64 computing “cores” that run simultaneously. Unfortunately, it
turns out that writing high-speed code to take advantage of processor
parallelism is really hard. The Parallel Computing Lab is basically entirely
funded by companies like Microsoft and Intel to figure out how make it
possible for non-superstar programmers to write good (or even merely
non-buggy) parallel programs. The point of the boot camp was to spread some of
the wisdom that the Parallel Lab folks have gained to a broad spectrum of
programmers, both scientific and commercial, who think they might need it.

This was the first edition of the boot camp, so there were some rough edges to
it, but it was overall a worthwhile experience. (Though that’s not a terribly
high bar when registration is free for UC Berkeley students and the course
took place just a few buildings over from mine.) Not knowing much about
parallel computing, it was good to get an overview of the state of the art and
the basic frameworks that are out there. It was somewhat comforting to see
that there don’t appear to be any major important conceptual foundations to
parallel programming that I’m unfamiliar with.  On the other hand it would
have been nice to have discovered that while I wasn’t looking someone had
figured out how to make it really easy to write fast, correct parallel
programs.

My personal interest in this topic, besides a desire to stay informed about
these sorts of things, is that I’d like to learn more about how to analyze
radio astronomy data in a parallel computing environment. A lot of the work
that I do involves a lot of waiting around for observations to be processed,
and it’d be a big win to be able to significantly decrease the amount of time
spent doing that. One challenge particular to radio astronomy is that a lot of
the problems discussed by parallel computing people are all about crunching a
_relatively_ small set of numbers: simulating particles in a box, doing linear
algebra, etc. A lot of the radio astronomy applications, on the other hand,
involve running through large datasets, so you want to read them from and
write them to disk as fast as you possibly can.  The Berkeley theory group and
Radio Astronomy Lab have won a contract to build a pretty good-sized parallel
computing cluster, so there will be an opportunity to explore these things
over the next few years. Doing so would require all-new software, but I think
it’s a really interesting problem with the potential for big gains. As the
computer scientists say, “a quantitative change of an order of magnitude is a
qualitative change” — if you can make a tool faster by a factor of 10, that
really changes the ways in which you use it. I’m hopeful that I’ll get the
chance to spend some more time on this over the next few years.
