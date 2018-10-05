+++
date = 2014-05-21T10:55:41Z
title = "scipy.stats Cheat Sheet"

[extra]
wp_rel_permalink = "/2014/05/scipy-stats-cheat-sheet/"
wp_shortlink = "/?p=873"
+++

Key methods of the distribution classes in `scipy.stats`.

- *pdf* — probability density function
  - Probability of obtaining `x < q < x + dx` is `pdf(x) dx`
  - Derivative of CDF
  - Goes to 0 at ±∞ for anything not insane
  - Not invertible because it’s hump-shaped!

- *cdf* — cumulative distribution function
  - Probability of obtaining `q < x` is `cdf(x)`
  - Integral of CDF
  - Invertible (to the PPf)
  - `CDF = 1 – SF`
  - `cdf(-∞) = 0`
  - `cdf(+∞) = 1`

- *ppf* — percent-point function (inverse CDF)
  - If many samples are drawn, a fraction _z_ will have values `q < ppf(z)`.
  - PPF = inverse of CDF
  - Domain is zero to unity, inclusive; range indeterminate, possibly infinite.

- *sf* — survival function
  - Probability of obtaining `q > x` is `sf(x)`
  - `SF = 1 – CDF`
  - `sf(-∞) = 1`
  - `sf(+∞) = 0`

- *isf* — inverse survival function
  - If many samples are drawn, a fraction _z_ will have values `q > ppf(z)`.
  - ISF = inverse of SF (duh)
  - Domain is zero to unity, inclusive; range indeterminate, possibly infinite.

There also exist *logpdf*, *logcdf*, and *logsf*, with the intuitive definitions.
