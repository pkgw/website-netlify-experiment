+++
date = 2013-04-03T23:23:15Z
title = "Propagating Uncertainties: The Lazy and Absurd Way"
path = "2013/04/propagating-uncertainties-the-lazy-and-absurd-way"

[extra]
wp_rel_permalink = "/2013/04/propagating-uncertainties-the-lazy-and-absurd-way/"
wp_shortlink = "/?p=660"
+++

I needed to write some code that does calculations and propagates
uncertainties under a fairly generic set of conditions. A well-explored
problem, surely? And indeed, in Python there’s the
[`uncertainties` package](http://pythonhosted.org/uncertainties/) which is
quite sophisticated and seems to be the gold standard for this kind of thing.

Being eminently reasonable, `uncertainties` represents uncertain variables
with a mean and standard deviation, propagating errors analytically. It does
this quite robustly,
[computing the needed derivatives magically](http://pythonhosted.org/uncertainties/tech_guide.html#differentiation-method),
but analytic propagation still fundamentally operates by ignoring nonlinear
terms, which means, in the words of the
[`uncertainties` documentation](http://pythonhosted.org/uncertainties/tech_guide.html),
that “it is therefore important that uncertainties be small.” As far as I can
tell, `uncertainties` does analytic propagation as well as anything out there,
but honestly, if your method can’t handle large uncertainties, it’s pretty
useless for astronomy.

Well, if analytic error propagation doesn’t work, I guess we have to do it
empirically.

So I wrote [a little Python module](https://gist.github.com/pkgw/5307284). To
represent 5 ± 3 I don’t create a variable that stores `mean=5` and `stddev=3`
— I create an array that stores 1024 samples drawn from a normal distribution.
Yep. To do math on it, I just use [`numpy`](http://www.numpy.org/)‘s
vectorized operations. When I report a result, I look at the 16th, 50th, and
84th percentile points of the resulting distribution.

Ridiculous? Yes. Inefficient? Oh yes. Effective? _Also_ yes, in many cases.

For instance: the `uncertainties` package doesn’t support asymmetric error
bars or upper limits. My understanding is that these could be implemented, but
they badly break the assumptions of analytic error propagation — an asymmetric
error bar _by definition_ cannot be represented by a simple mean and standard
deviation, and an upper limit measurement _by definition_ has a large
uncertainty compared to its best value. But I can do math with these values
simply by drawing my 1024 samples from the right distribution —
[skew normal](http://en.wikipedia.org/wiki/Skew_normal_distribution) or
uniform between zero and the limit. I can mix perfectly-known values,
“standard” (i.e. normally-distributed) uncertain values, upper limits, and
anything else, and everything Just Works. (It might be hard to define the
“uncertainty” on a complex function of a mixture of all of these, but that’s
because it’s genuinely poorly-defined — analytic propagation is just
misleading you!)

Another example: `uncertainties` spends a lot of effort tracking correlations,
so that if `x = 5 ± 3`, then `x - x = 0` precisely, not 0 ± 4.2. My approach
gets this for free.

I’ve found that approaching uncertainties this way helps clarify your thinking
too. You worry: is 1024 samples big enough? Well, did you actually measure 5 ±
3 by taking 1024 samples? Probably not. As
[Boss Hogg](http://cosmo.nyu.edu/hogg/) points out,
[the uncertainties on your uncertainties are large](http://hoggresearch.blogspot.com/2009/11/bayesian-spectrum-analysis.html).
I’m pretty sure that only in _extreme_ circumstances would the number of
samples actually limit your ability to understand your uncertainties.

Likewise: what if you’re trying to compute `log(x)` for `x = 9 ± 3`? With 1024
samples, you’ll quite likely end up trying to take the logarithm of a negative
number. Well, _that’s telling you something_. In many such cases, `x` is
something like a luminosity, and while you might not be confident that it’s
much larger than zero, I can _guarantee_ you it’s not actually less than zero.
The assumption that x is drawn from a normal distribution is failing. Now,
living in the real world, you want to try to handle these corner cases, but if
they happen persistently, you’re being told that the breakdown of the
assumption is a significant enough effect that you need to figure out what to
do about it.

Now obviously this approach has some severe drawbacks. But it was _super_ easy
to implement and has Just Worked remarkably well. Those are big deals.
