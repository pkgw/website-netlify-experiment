+++
date = 2008-05-08T22:48:27Z
title = "Not flagging!"

[extra]
wp_rel_permalink = "/2008/05/not-flagging/"
wp_shortlink = "/?p=69"
+++

Been a little while since I’ve remembered to update this …

Lately I’ve been continuing to work on the data that I’ve obtained for my
broadband spectra project. After spending a fairly long time on the flagging
component of things, I arrived at a point where I think I can pretty reliably
mask out the bad data. So I turned my attention to reliably measuring
brightnesses from the data.

There are a couple of ways you can approach this. An interferometer yields
data in “the UV domain”, that is, you don’t get a picture of the sky straight
out. Instead, you get something a bit more complicated: a bunch of discrete
samples of the Fourier transform of the image of the sky that your telescope
was pointed at (plus noise, plus infidelities due to the apparatus, plus
interference). The data aren’t directly understandable as a picture, but they
do hold a well-defined relationship to the objects you were looking at.
Anyway, one way to measure brightnesses is to use the UV-domain data and find
a mathematical fit to what a bright source would look like in the UV domain,
and one of the parameters you solve for is the source’s brightness.
Unfortunately, this is imperfect, because there are always background sources,
diffuse emission, and other things in the sky whose emission you’re capturing.
The way in which these things affect your UV data is well-understood, but a
simple fitting algorithm doesn’t take them into account, and the brightnesses
that you solve for are systematically biased because of them.

A different way to find brightnesses is to transform the UV domain data into
an image. This is a bit of a complex process, but it’s what you do with
interferometers 99% of the time, so the algorithms to do it are known,
commonly implemented, and well-tested. Of course, you’d prefer not to put your
data through a complex processing step if you can avoid it, but it’s nice to
have an image because measuring brightnesses from images is pretty
straightforward. You look at the bright thing in the middle, do another
mathematical fit with the known way that single points appear in images, and
get your answer. This answer is more robust because your background
contaminants are in different parts of your image and can be screened out much
more easily than is the case with UV domain data.

So. I had code to measure brightnesses using both methods, but unfortunately
the results were disagreeing badly. The background problem in the UV domain is
an issue, but it’s not large enough to cause the kind of disagreements that I
was seeing. This was a little scary.

Looking at my UV data, I realized that the amplitudes I was getting —  which
should correspond directly to the brightness you get — were varying
substantially depending on which pair of antennas was generating them. This
affects your UV results, because there’s no guarantee that the variations
average out the right answer, and it affects your image results, because the
varying amplitudes work out to brightness being misplaced in the image when
you generate one.

One reason for these varying amplitudes became clear. With the Fx64
correlator, we have to integrate up data for a relatively long time (7.5
seconds) because we generate a lot more data than we used to and it just takes
a long time to write them all to disk. One unfortunate side effect of
integrating like this, though, is that our measurements effectively become
diluted. This is due to an effect called “fringe rotation”. Basically, the
fact that the Earth is spinning causes the values we measure to cycle around,
and if you integrate over an appreciable fraction of a cycle, your values
start adding up to zero. Taking quicker snapshots is better, in this case.

Fortunately, the damping effect cause by fringe rotation is predictable, so in
theory you can correct for it. You’d still rather not have it at all — a
damped signal means that the inherent system noise is relatively larger — but
you can at least try to correct the data so that doing things like creating
images gives you what you want.

Unfortunately, when I wrote a routine to correct my data for this, it corrects
things pretty well, but not perfectly. There’s still some other factor
affecting the amplitudes I get, and my correction routine blows up the
unaccounted-for changes and yields data that aren’t any better than the ones I
started with.

So, right now, I’m working on figuring out what else is messing up my
amplitudes, and seeing if I can eliminate it. Next post (I feel like a blogger
now!) I can discuss what the suspects are and what I’m investigating. Also, I
should get around to explaining just what flagging is all about.
