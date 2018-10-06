+++
date = 2007-09-23T21:08:13Z
title = "Attack of the ATA"
path = "2007/09/attack-of-the-ata"

[extra]
wp_rel_permalink = "/2007/09/attack-of-the-ata/"
wp_shortlink = "/?p=21"
+++

Right. So. I’m about halfway into my weeklong stay at the ATA. Lonely weekend
what with the … no one else being here. But it hasn’t been breaking, and I
haven’t been bored. Would be nice to be not-working as opposed to working,
though, but I’ll make up for that once I’m back home.

Thursday was basically devoted to getting here. The drive went relatively
quickly, I think, but that was still four and a half hours. Didn’t need to
spend much time getting oriented since I remembered the setup from my previous
trip pretty well.

Friday was spent having Rick show me the ropes. The systems seem pretty well-
designed — at least, I find the usual operations pretty easy to understand or
figure out. The problem, of course, is that the _un_usual operations are where
experience like Rick’s is important, and it’s just not possible for him to
pass that on to me in a day. Hopefully, nothing wacky will happen and it won’t
be an issue. But I’ve been trying to glance at the data coming in, and some of
it is kind of scary-looking. My fear is that there’s something wrong with the
hardware or software that I’m not quite on the ball enough to recognize. Or
maybe the data’s fine, or maybe there’s nothing I can do about it. After all
it was raining yesterday and stuff, and I don’t care how transparent water is
at our wavelengths, that’s gotta hurt your observations.

We ran some canned observations on Friday. On Saturday, I ran the first day of
Geoff’s observing program at day and began mine at night. Me being me, I wrote
my observing script in Python with some hacks to bridge it to the existing
infrastructure. I spent a while pondering things and any shell script
implementation would have had a _lot_ of cut-and-paste code and a lot of hacks
to get around the fact that you can’t freaking do math in shell. The pain of
trying to easily communicate with subprocesses in Python _almost_ outweighs
those problems, but unlike CSH, Python has these fancy things called
functions, so I can solve that problem once and be done with it. Which is what
I did. The script ran fine on the first try and I finished writing it (just)
before my observing block started. So there. I haven’t looked at the data but
if there are problems there it’s not Python’s fault.

Today, I ran the second day of Geoff’s program and worked on a tweaked version
of my observing script. We’re not exactly oversubscribed at the moment, so I’m
going to try two versions of my program and see what works out better. I also
scheduled the rest of this week’s proposals and started working on a way to
automatically calibrate the PAM settings of the antennas. I had scheduled my
second block to start immediately after Geoff’s finishes, but I think I’ll
take my PAM observations; then I can spend a while working on the analysis of
that while my and Geoff’s observations run. And the PAM stuff should only take
an hour or so, so I can still get a lot of data on my proposal.

Also iterated with The Other Geoff a bunch on the lab for this week in 120. I
think it’s pretty good. I always hate it when things like labs are vague about
what results they want you to give, so I tried to be super specific about
those parts. We’ll see how well I did. I’d feel better if I’d done the whole
lab before having the students do it, but I’m pretty sure that it’s not very
“hey this is impossible”-prone.

So, tomorrow will probably involve doing the hard part of the PAM setting
stuff. I’ll have to figure out how to extract gains from Miriad data without
the help of my sketchy little Python stack. Also, the work week is starting
up, and I’m not sure how much time I’ll spend responding to other people
needing to take antennas offline or whatever. But besides those, the entire
day is scheduled, so if things behave themselves I’ll probably have a lot of
free time. To work on Star Formation homework!
