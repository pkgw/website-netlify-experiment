+++
date = 2014-04-29T00:00:00-04:00
title = "Change Variables in an Integral"
weight = 0 # all howtos have zero weight => alphabetical ordering
template = "howto.html"
+++

Because I can never friggin’ remember. Here’s an example:

```
K = \int_1^2 x dx = 3/2
```

OK.

```
z = e^x
x = ln z
dx = dz / z
K = \int_e^{e^2} (ln z) (dz / z)
```

Which indeed numerically evaluates to the right thing.

That is, given an integral in terms of `x`, and wishing to change to `f(x)`:

1. Let `g = (f inverse)`: such that `x = g(z)`.
2. Replace integrand using `g` and `dg/dz`.
3. Replace limits `a`, `b` with `f(a)`, `f(b)`. Dimensionally, it must be so.
