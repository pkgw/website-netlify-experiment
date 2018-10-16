+++
date = 2013-06-13T23:30:02-04:00
title = "Match Up a Histogram and a Normal Distribution"
weight = 0 # all howtos have zero weight => alphabetical ordering
template = "howto.html"
+++

Given some data that have been histogrammed, how do we overplot the normal
distribution that represents the maximum likelihood parameters of the
underlying unbinned data? The key is getting the normalization right, and the
key to that is that we can compute the area under both the histogram and the
distribution.

Given data *d* and *nbins*:

```python
m = d.mean()
s = d.std()
xmin = d.min()  # these bounds can be tweaked
xmax = d.max()
x = np.linspace(xmin, xmax, 512)  # the 512 is also adjustable
norm = d.size * (xmax - xmin) / (nbins * np.sqrt(2 * np.pi) * s)
y = norm * np.exp(-0.5 * ((x - m) / s)**2)
```
