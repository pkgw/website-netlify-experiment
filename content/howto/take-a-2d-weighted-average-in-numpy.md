+++
date = 2018-10-15T17:25:06-04:00
title = "Take a 2D weighted average in Numpy"
weight = 0 # all howtos have zero weight => alphabetical ordering
template = "howto.html"
+++

<!-- Written for Russell Van Linge and dftdynspec. -->

Say that you have a 2D image stored as a [Numpy](http://www.numpy.org/) array.
Along with the data themselves, you also have a noise image of the uncertainty
associated with each pixel. You’d like to bin your image along both axes to
increase your signal-to-noise. How does one go about that?

I don’t know of one single preferred tool for doing such averaging — you more
or less have to roll your own code. I’ll give the 80% solution here. It's a
bit tricky to cover all possible corner cases, but the basic operations should
hopefully seem straightforward if you've taken a data analysis class. There's
one sneaky trick to writing efficient Python code to do the operation, though.

Fundamentally you want to take a weighted average, where the weight that you
use is the inverse *variance* of each measurement — that is, the inverse of
the squares of the standard deviations. Starting with the most straightforward
case, imagine you have an array of *n* uncertain measurements, and you want to
take their weighted average in this way. We can write:

```python
# "data" is the array of measurements. "uncerts" is the array
# of their uncertainties / standard deviations.
data = [....]
uncerts = [...]

# "weights" are the weights to use when averaging: inverse variances.
weights = uncerts ** -2

# This is how you take a weighted average:
wt_avg = (data * weights).sum() / weights.sum()

# And if you work out the stats, this is the uncertainty
# of "wt_avg" when things are well-behaved:
uncert_wt_avg = 1 / np.sqrt(weights.sum())
```

For the first wrinkle, imagine that you have an array of 80 numbers, and you
want to take the weighted average of in groups of 10 numbers — eight groups in
all. The clever trick is that you can do this efficiently by using the
`np.reshape()` function to pretend that your array is two-dimensional, and
then using the `axis=` optional argument to the `sum()` function to only sum
over one axis:

```python
# We have 80 measurements and 80 uncerts; nonsense values
# used here
data = np.random.normal(size=80)
uncerts = np.ones(80)

# Re-interpret the arrays as 8-by-10 2D arrays
r_data = data.reshape((8, 10))
r_uncerts = uncerts.reshape((8, 10))

# Proceed as before, but only sum along one axis each time. We sum
# along the 1-th axis, which is counted starting from zero -- so
# we're summing along the rightmost axis, the one of size 10.
r_weights = r_uncerts ** -2
wt_avg = (r_data * r_weights).sum(axis=1) / r_weights.sum(axis=1)
uncert_wt_avg = 1 / np.sqrt(r_weights.sum(axis=1))
```

If you run the above code, you should find that `wt_avg` and `uncert_wt_avg`
are 8-element 1D arrays, as intended.

You can use the same basic trick for a 2D image by turning it
*four*-dimensional. The resulting code is very similar. Say we have an
80-by-120 image that we want to bin by 10 pixels along both dimensions:

```python
# Data and uncertainty images
data = np.random.normal(size=(80, 120))
uncerts = np.ones((80, 120))

# Re-interpret as 4D
r_data = data.reshape((8, 10, 12, 10))
r_uncerts = uncerts.reshape((8, 10, 12, 10))

# Proceed as before, but now sum along two axes.
r_weights = r_uncerts ** -2
wt_avg = (r_data *
          r_weights).sum(axis=(1,3)) / r_weights.sum(axis=(1,3))
uncert_wt_avg = 1 / np.sqrt(r_weights.sum(axis=(1, 3)))
```

Finally, things are often trickier in the real world since your array
dimensions might not be so neatly divisible into groups. The most convenient
thing to do is drop a few samples off the edges of your arrays if needed.
There’s no single “best” way to do so: I usually end up experimenting with
numbers to trade off between how big I want each bin to be, and how many
samples I’m comfortable discarding. Given a target bin size on each axis,
though, here’s a sketch of how you might chop your arrays down to the desired
size:

```python
def chop_and_reshape_array(arr, y_bin_size, x_bin_size):
    ny, nx = arr.shape
    n_y_bins = ny // y_bin_size
    n_x_bins = nx // x_bin_size
    arr = arr[:n_y_bins * y_bin_size,
              :n_x_bins * x_bin_size]
    return arr.reshape((n_y_bins, y_bin_size, n_x_bins, x_bin_size))
```

Here we are using my preferred convention of mentally labeling the two axes of
a 2D array `[y, x]`: this corresponds to how 2D arrays are visualized in
Python.
