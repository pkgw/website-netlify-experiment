+++
date = 2014-03-24T00:00:00-04:00
title = "Sample from a Gaussian Process"
weight = 0 # all howtos have zero weight => alphabetical ordering
template = "howto.html"
+++

Because apparently this is a challenge for me.

Cf.
[this stackexchange answer](https://stats.stackexchange.com/questions/32169/how-can-i-generate-data-with-a-prespecified-correlation-matrix):
given a random vector *x* sampled from a Gaussian distribution with mean *m*
and covariance *C*, and also given matrix *A*, then *(A.x)* has mean *(A.m)*
and covariance *(A.C.A^T)*. If we’re drawing uncorrelated samples with mean
zero and variance 1, then C is the identity matrix.

So, given such a sample, if we want to achieve a covariance matrix *D*, we
need *A* such that *A.A^T = D*. One incarnation of such is the Cholesky
decomposition of *D*. *D* must be positive definite for the decomposition to
exist, but it must also be that to be a valid covariance matrix. We must
augment the diagonal of *D* to achieve this condition (i.e., include the
individual measurement error term).

If we’re using the squared exponential GP kernel, we have:

```python
x = np.linspace(0, 10, 100)
r = x[None,:] - x[:,None]
cov = np.exp(-0.5 * r**2 / 1**2) + np.eye(100) * 1e-6
chol = np.linalg.cholesky(cov)
y = np.dot(chol, np.random.normal(size=x.size))
```

(Note: without the diagonal term added here, the determinant of `cov` is
precisely zero. So yeah, we just need to add something miniscule to bump it up
to be positive. i think. I don’t know a ton about linear algebra …)

How to we verify that we did it right? I’m pretty sure we have to draw a bunch
of sample *y* values.

```python
t = np.dot(chol, np.random.normal(size=(x.size, 300)))
z = np.cov(t) # rowvar=False changes output significantly!
z.shape == (100, 100) # -> True, duh.
```

An `ndshow.view()` of *z* should give similar structure to `cov`, and modeling
should yield parameters compatible with the inputs used to generate `cov`
(lengthscale = 1, measurement σ = 1e-3, here).
