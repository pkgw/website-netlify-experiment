+++
date = 2017-07-18T22:28:21Z
title = "“Variable and polarized radio emission from the T6 brown dwarf WISEP J112254.73+255021.5”"

[extra]
wp_rel_permalink = "/2017/07/variable-and-polarized-radio-emission-from-the-t6-brown-dwarf-wisep-j112254-73255021-5/"
wp_shortlink = "/?p=1034"
+++

I should post something about this paper — it only
[came out on Arxiv](https://arxiv.org/abs/1608.04390) eleven months ago. What
can I say, it’s been a busy year! Here’s the
[official journal version](https://dx.doi.org/10.3847/1538-4357/834/2/117).

This paper was inspired by a
[neat result from Matt Route & Alex Wolszczan](https://dx.doi.org/10.3847/2041-8205/821/2/L21)
that came out last year
([free Arxiv version here](https://arxiv.org/abs/1604.04543)). They detected
yet another radio-emitting brown dwarf with [Arecibo](http://www.naic.edu/),
adding to the very small number of T-type brown dwarfs detected in the radio.
These objects are fascinating because they’re at the cutting edge of what we
can detect with current facilities — they are the physical size of planets
like Jupiter, and not _that_ much more massive. Radio observations tell us
about the magnetic fields of these objects, and
[I’ve argued recently](https://arxiv.org/abs/1707.04264) that the takeaway is
that these brown dwarfs have magnetic fields that are basically like amped-up
versions of the one we find around Jupiter and the Earth. Which is cool
because Jupiter’s magnetic field turns out to be _bananas_ as well as very
important scientifically — it drives immensely complex space plasma physics
and tells us about Jupiter’s internal structure. Studies of T-type brown
dwarfs give us the first glimpse of what the magnetic fields of planets around
other stars might look like.

Not only did Route & Wolszczan discover an interesting new object — full name
WISEP J112254.73+255021.5, “WISE 1122+25” for short — they made a bold claim:
that it might be rotating as rapidly as one full revolution every 18 minutes.
Keep in mind that this is a ball of gas the size of Jupiter. You can do the
calculations and it’s not physically impossible for WISE 1122+25 to rotate
that quickly, but only just barely. This thing would be dramatically
egg-shaped, and who knows what kind of neat physical effects that would cause.

Route & Wolszczan made their conjecture based on the timing of when they
detected bursts of radio waves from WISE 1122+25. If the bursts are sweeping
past us like the beam of light from a lighthouse, their periodicity tells us
about how long it takes the object to make a complete spin. Unfortunately, the
data weren’t definitive — there were only five bursts detected over a span of
months. If every burst arrives at a _perfectly_ rigid cadence, you can still
measure a rotation period, but with that few bursts spread over that long of a
time, you worry about any periodic signals being spurious.

It’s definitely a neat possibility, though! So,
[as has happened before](https://arxiv.org/abs/1301.2321), I teamed up with
some of my regular collaborators,
[John Gizis](http://www.physics.udel.edu/~gizis/) and
[Edo Berger](https://scholar.harvard.edu/eberger/home), to observe
WISE 1122+25 with the
[NRAO Very Large Array](https://public.nrao.edu/telescopes/vla/) (the
[legendary](https://en.wikipedia.org/wiki/Contact_(1997_American_film)#/media/File:Contact_ver2.jpg)
“VLA”) and see if we could verify the claims. Arecibo is better at detecting
very rapid bursts than the VLA, but the VLA can sit on one object for longer
and detect fainter events — perfect for checking whether we could, say, see
any bursts happening every 18 minutes like clockwork. We got these
observations through the VLA Director’s Discretionary Time channel — thanks to
the Director!

And what did we find? The image below shows how the
radio brightness varies over the course of several hours, with the radio
emission being broken down in several different ways.

![VLA radio light curve of WISE 1122+25](https://newton.cx/~peter/wp/wp-content/uploads/2017/07/xenia-vla-1024x854.png)

I won’t describe the data in detail, but the first big takeaway is that we do
_not_ see evidence for periodic signals every 18 minutes or so. A more formal
periodogram analysis supports this conclusion, and we don’t see any evidence
for variation in optical data either. Overall, these data make us think that
the 18-minute periodicity found by Route & Wolszczan was spurious.

But we _do_ see a lot of complicated variability in the radio emission! What I
found to be the most exciting was the measurement shown in the lowest panel of
the figure above. It shows the level of
[circular polarization](https://en.wikipedia.org/wiki/Circular_polarization)
of the radio waves we get from WISE 1122+25. Almost all astronomical objects
emit light that is unpolarized in the circular sense — that is, 0% circular
polarization. Radio-emitting brown dwarfs are among the rare objects that can
produce high levels of circular polarization. The way we quantify things,
circular polarization levels can range between +100%, meaning fully _right-
handed_ circular polarization, to –100%, for fully _left-handed_ circular
polarization.

What’s neat about the VLA data is that the polarization fraction seems to
swing back and forth between the two states. We’ve seen brown dwarfs emit
radio bursts with both kinds of handedness, but I’m not aware of any data
showing these kind of long-lasting, abrupt transitions. And if you get a bit
ambitious in the interpretation, you can imagine that maybe this handedness
flips back periodically with the rotation of the brown dwarf. Looking at the
different pieces of data, we found some evidence for periodicity at 116
minutes. But the whole observation only spanned 162 minutes, so that’s a very
tentative idea — you’d want to see multiple flips back and forth all in
sequence to be more confident.

But … if you want to get even **more** ambitious … You might be able to
explain that kind of behavior if this object has a magnetic field that has a
major axis that’s very misaligned with the rotation axis. With the right
viewing geometry and magnetic polar caps that emitted strongly polarized
radiation, you can get curves that look similar to the data.

You don’t have to take my word for it! Here’s an interactive
simulator I put together that shows the scenario. You can drag the sliders
around to adjust the key physical parameters of the (very simplistic) model.
“LOC” is the “latitude of center”, which is how inclined the object’s equator
is relative to the viewer. “CML” is “central meridian longitude”, which tracks
where we are in a rotation of the object. The other two sliders set the size
of the magnetic caps and their separation from the rotation axis.

<iframe src="https://newton.cx/~peter/wp/wp-content/uploads/2017/07/xenia/interactive.html" width="100%" height="400px" scrolling="yes" class="iframe-class" frameborder="0"></iframe>

On the right-hand side, the solid line is the total brightness and the dashed
line is the fractional polarization. If you set LOC = 25 and θ = 50, you get
curves that resemble the VLA data … if you squint, and get enthusiastic about
the possibility that the emission might be repetitive every two hours, at
least. It’s hard to see how the magnetic field would end up so misaligned with
the object’s rotation, so it’d be really interesting if this was the case!

As always, what we need is more data. I’ve obtained more, longer observations,
and am in the process of analyzing them now. Stay tuned!
