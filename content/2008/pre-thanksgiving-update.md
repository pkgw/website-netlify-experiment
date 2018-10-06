+++
date = 2008-11-23T17:28:08Z
title = "Pre-Thanksgiving Update"
path = "2008/11/pre-thanksgiving-update"

[extra]
wp_rel_permalink = "/2008/11/pre-thanksgiving-update/"
wp_shortlink = "/?p=95"
+++

Progress continues to be slow, but measurable, with the broadband spectra
project.

During discussions with Geoff, he repeated a fact that I’d really failed to
fully appreciate: a key aspect of this project is demonstrating that the
results I get are reliable and reproducible.

This wasn’t news to me, but it had always seemed to me to be both obvious and
vague. Clearly, you want reproducible and reliable results, but how do you go
about showing that? When Geoff mentioned this goal most recently, though, I
had the thought that I have an easy way to show reliability that I’ve been
completely failing to take advantage of. I haven’t been cross-checking my
results at all. All of my measurements are relative to one calibrator or
another: measure calibrator A, observe source X, get brightness X(A). Measure
calibrator B, observe source Y, get brightness Y(B). But I’ve basically
neglected to do the obvious pairing of measuring calibrator B, observing
source X, and getting brightness X(B). If systematics are controlled and
uncertainties are understood, X(A) and X(B) should agree to within their
uncertainties.

Unfortunately, a lot of my data don’t have multiple calibrators available,
purely as a side effect of what is visible at any given time. But I certainly
have a fair amount of data that can be used for this kind of cross-checking.

I started pursuing this idea and obtained a pretty nice result fairly quickly.
I soon realized that the measurements I was getting based on the calibrator
3c48 were fairly discrepant from the other ones. I looked into this and, lo
and behold, the model I was using for 3c48 wasn’t accurate, and better values
that I obtained were different in almost exactly the way my measurements
indicated they needed to be. That was encouraging.

Even better, I remembered that the ATA has a _large_ library of archival
long-duration calibrator observations. I can use these data to  test out my
processing pipeline and do the kinds of cross- checks mentioned above. I can
also assess the stability of my results in general and look for other issues.

Already, I found one further problem: for a long time, I’ve been normalizing
my results by dividing my crosscorrelations by my autocorrelations. This has
some helpful effects, but looking at the calibrator observations revealed to
me that the autocorrelations will drift up and down in ways not seen in the
cross-correlations, damaging my amplitude calibration. Stopping this practice
seems to improve my results even more, though I haven’t reprocessed everything
yet.

I was sick at the end of last week, so work slowed down a bit, but I hope to
keep on pushing this. I believe there’s at least one more nontrivial
systematic effect to deal with, but even that one may not be significant
enough to affect my results. If I can figure out how to compensate for it,
though, I think my reduction process will be in extremely good shape.
