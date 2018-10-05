+++
date = 2012-06-07T16:07:06Z
title = "Poisson Distribution Confidence Intervals in Scipy"

[extra]
wp_rel_permalink = "/2012/06/poisson-distribution-confidence-intervals/"
wp_shortlink = "/?p=556"
+++

As happens often when doing transient searches, lately I’ve found myself
wanting to compute confidence intervals in rate measurements from a small
number of events. Clearly I want to be using the properties of the [Poisson
distribution](http://en.wikipedia.org/wiki/Poisson_distribution), but how so,
exactly?

The “Parameter Estimation” section of the above Wikipedia page gives some
hints but involves a few notation switches and also special functions that
don’t seem to be implemented in the handy
[`scipy.special`](http://docs.scipy.org/doc/scipy/reference/special.html) or
[`scipy.stats`](http://docs.scipy.org/doc/scipy/reference/stats.html)`
modules. Once you track down the notation, though, it turns out to be really
easy. We want the inverse incomplete regularized Γ function.

Let’s say you observe _n_ events in a period and want to compute the _k_
confidence interval on the true rate — that is, 0 < _k_ ≤ 1, and _k_ = 0.95
would be the equivalent of 2σ. Let _a_ = 1 − _k_, _i.e._ 0.05. The lower bound
of the confidence interval, expressed as a potential number of events, is

```python
scipy.special.gammaincinv(n, 0.5 * a)
```

and the upper bound is

```python
scipy.special.gammaincinv(n + 1, 1 - 0.5 * a)
```

Conversion to rates is then just a matter of dividing by the relevant
duration, area, whatever. These apparently give the “exact” interval which may
be minutely more strict than is necessary. The halving of _a_ is just because
the 95% confidence interval is made up of two tails of 2.5% each, so the
`gammaincinv` function is really, once you chop through the obscurity, exactly
what you want.

So in
[this example](http://www.statsdirect.com/help/rates/poisson_rate_confidence_interval.htm),
_n_ is 14, _a_ is 0.05, and we divide by 400 to get the interval bounds as
reported (0.019135 to 0.058724, in case that webpage disappears).

It took me a while to understand the numbers in the first table
[on this page](http://www.math.mcmaster.ca/peter/s743/poissonalpha.html), but
they’re very helpful once you get over that: they give the 95% confidence
limits for a given number of observed events, when that number is small.
_I.e._, if I observe one event over some period, my 95% confidence interval is
0.0253 to 5.5616 events. These numbers don’t quite make sense on their own,
since you can only get integral numbers of events in practice, but you can use
them to compute rate limits that _are_ perfectly meaningful.

(Once you think about it, the relationship between the expressions for the two
ends of the interval is kind of cute. Because the Poisson distribution can
only take on integral values, the 2.5% upper limit to the value _n_ must be
the 2.5% lower limit to the value _n_ + 1, because there are no intervening
values that can be chosen.)
