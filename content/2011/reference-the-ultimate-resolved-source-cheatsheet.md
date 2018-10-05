+++
date = 2011-12-07T23:52:04Z
title = "Reference: The Ultimate Resolved Source Cheatsheet"

[extra]
wp_rel_permalink = "/2011/12/reference-the-ultimate-resolved-source-cheatsheet/"
wp_shortlink = "/?p=488"
+++

OK, this isn’t actually the _ultimate_ resolved source cheatsheet … yet. I’m
just trying to centralize my notes on dealing with extended sources. I’ve been
doing this lately, and I had to rederive a bunch of things that I know I’ve
figured out before. Hopefully, next time I’ll remember that I wrote all this
stuff down here.

# Units

Radio astronomical images typically come in two unit systems: Jy/pixel and
Jy/beam. For various questions one usually wants to convert to Jy/arcsec² or
Jy/sr. _Jy/pixel is not trivially equivalent to Jy/arcsec², because the pixel
size can change as a function of position in many map projections.

There must be something profound about why maps come in Jy/bm and models come
in Jy/pixel, but I don’t see it right now.

Source fluxes are best measured as _total fluxes_ which come in units of plain
_Jy_. This should be obvious! Flux is conserved! In the general case _peak_
fluxes are always dependent on the image properties.

The important exception, however, is _unresolved_ sources which by their
nature have a peak flux equal to their total flux no matter what unit system
you’re using. Total flux of 1 Jy, peak flux of 1 Jy/px spread over 1 pixel, or
peak flux of 1 Jy/bm spread out over 1 beam.

_Resolved_ sources will have a peak flux that depends on the particular image
units and projection, because the total flux will be spread out over a number
of pixels that depends on the image particulars. In a Jy/px image, you need to
figure out how many pixels the source subtends, and _mutatis mutandis_ for
Jy/bm. Generically, `pkflux = totflux * arcsec2perpix / arcsec2insource`. If
you have a 2D Gaussian source where the axes are FWHMs in arcsec,
`arcsec2insource = 2 pi major minor / (8 ln 2)`.

I _think_ the best way to work with Jy/bm is to go through Jy/px: the beam
volume in pixels can be derived from the beam parameters and the pixel volume:
`pixperbm = arcsec2perbm / arcsec2perpix`. For various operation I feel like
this quantity will cancel out, though. Once again, due to the
position-dependent pixel volume in most maps, this parameter is not constant
across the map.

# 2D Gaussian Parametrizations

There are a few ways to parametrize a 2D Gaussian. I’ll omit centering and
overall scaling in the following equations for simplicity.

**Tersest.** The simplest expression in
terms of symbols is:

![z = \exp\left(Ax^2 + Bxy + Cy^2\right)](https://s0.wp.com/latex.php?latex=z+%3D+%5Cexp%5Cleft%28Ax%5E2+%2B+Bxy+%2B+Cy%5E2%5Cright%29&bg=ffffff&fg=000000&s=0 "z = \exp\left(Ax^2 + Bxy + Cy^2\right)")

This parametrization is computationally efficient but not intuitive. One
particular danger to note is that the parameters behave a bit oddly, and there
are domain limitations that make it awkward for numerical optimizers (which
are likely to tweak the parameters outside of their domains): _A_ and _C_ must
be negative, and, if I’m doing my algebra right, you must have `B² < 4AC`.

**Mathematical Major/Minor/PA.** We often want to express the shape of the 2D Gaussian as a
major axis σ1, minor axis σ2, and position angle θ. Here σ1 ≥ σ2 > 0 and θ is
the rotation between the major axis and +x (with +θ being towards +y). Because
of the symmetry of the shape, there’s a 180° degeneracy in θ.  We find

![A = -\frac{1}{2}\left[\frac{\cos^2 \theta}{\sigma_1^2} + \frac{\sin^2 \theta}{\sigma_2^2}\right]](https://s0.wp.com/latex.php?latex=A+%3D+-%5Cfrac%7B1%7D%7B2%7D%5Cleft%5B%5Cfrac%7B%5Ccos%5E2+%5Ctheta%7D%7B%5Csigma_1%5E2%7D+%2B+%5Cfrac%7B%5Csin%5E2+%5Ctheta%7D%7B%5Csigma_2%5E2%7D%5Cright%5D&bg=ffffff&fg=000000&s=0 "A = -\frac{1}{2}\left[\frac{\cos^2 \theta}{\sigma_1^2} + \frac{\sin^2\theta}{\sigma_2^2}\right]")

,

![B = \sin \theta \cos\theta \left(\sigma_2^{-2}- \sigma_1^{-2}\right)](https://s0.wp.com/latex.php?latex=B+%3D+%5Csin+%5Ctheta+%5Ccos%5Ctheta+%5Cleft%28%5Csigma_2%5E%7B-2%7D+-+%5Csigma_1%5E%7B-2%7D%5Cright%29&bg=ffffff&fg=000000&s=0 "B = \sin \theta \cos\theta \left(\sigma_2^{-2}- \sigma_1^{-2}\right)")

, and

![C = -\frac{1}{2}\left[\frac{\sin^2\theta}{\sigma_1^2} + \frac{\cos^2 \theta}{\sigma_2^2}\right]](https://s0.wp.com/latex.php?latex=C+%3D+-%5Cfrac%7B1%7D%7B2%7D%5Cleft%5B%5Cfrac%7B%5Csin%5E2+%5Ctheta%7D%7B%5Csigma_1%5E2%7D+%2B+%5Cfrac%7B%5Ccos%5E2+%5Ctheta%7D%7B%5Csigma_2%5E2%7D%5Cright%5D&bg=ffffff&fg=000000&s=0 "C = -\frac{1}{2}\left[\frac{\sin^2 \theta}{\sigma_1^2} + \frac{\cos^2\theta}{\sigma_2^2}\right]")

. Note that if θ = 0, then

![z = \exp\left(-\frac{1}{2}\left[\frac{x^2}{\sigma_1^2} + \frac{y^2}{\sigma_2^2}\right]\right)](https://s0.wp.com/latex.php?latex=z+%3D%5Cexp%5Cleft%28-%5Cfrac%7B1%7D%7B2%7D%5Cleft%5B%5Cfrac%7Bx%5E2%7D%7B%5Csigma_1%5E2%7D+%2B+%5Cfrac%7By%5E2%7D%7B%5Csigma_2%5E2%7D%5Cright%5D%5Cright%29&bg=ffffff&fg=000000&s=0 "z=\exp\left(-\frac{1}{2}\left[\frac{x^2}{\sigma_1^2} +\frac{y^2}{\sigma_2^2}\right]\right)")

. Inverting, we find

![\theta = \frac{1}{2}\arctan \frac{B}{A-C}](https://s0.wp.com/latex.php?latex=%5Ctheta+%3D+%5Cfrac%7B1%7D%7B2%7D%5Carctan+%5Cfrac%7BB%7D%7BA-C%7D&bg=ffffff&fg=000000&s=0 "\theta = \frac{1}{2}\arctan \frac{B}{A-C}")

,

![\sigma_1^{-2} = -\sqrt{(A-C)^2 + B^2} - A - C](https://s0.wp.com/latex.php?latex=%5Csigma_1%5E%7B-2%7D+%3D+-%5Csqrt%7B%28A-C%29%5E2+%2B+B%5E2%7D+-+A+-+C&bg=ffffff&fg=000000&s=0 "\sigma_1^{-2} = -\sqrt{(A-C)^2 + B^2} - A - C")

, and

![\sigma_2^{-2} = +\sqrt{(A-C)^2 + B^2} - A - C](https://s0.wp.com/latex.php?latex=%5Csigma_2%5E%7B-2%7D+%3D+%2B%5Csqrt%7B%28A-C%29%5E2+%2B+B%5E2%7D+-+A+-+C&bg=ffffff&fg=000000&s=0 "\sigma_2^{-2} = +\sqrt{(A-C)^2 + B^2} - A - C")

. During a roundtrip, θ may flip by 180° depending on the numerics, but as
mentioned above this doesn’t change anything.

**Astronomical Major/Minor/PA.** This is the same as the above, except that by
the definition of PA, the _x_ axis is _declination_ and the _y_ axis is _right
ascension_. Be careful to write

![y = \exp \left (A\delta^2 + B\alpha \delta + C\alpha^2\right)](https://s0.wp.com/latex.php?latex=y+%3D+%5Cexp+%5Cleft+%28A%5Cdelta%5E2+%2B+B%5Calpha+%5Cdelta+%2B+C%5Calpha%5E2%5Cright%29&bg=ffffff&fg=000000&s=0 "y = \exp \left (A\delta^2 + B\alpha\delta + C\alpha^2\right)")

.

**Numerically-friendly.** If you’re fitting for
Gaussian parameters, it’s very helpful to numerical stability to have nice
continuous behavior over all of your parameters. The _B_ parameters above seem
to be problematic, so here’s a parametrization that is pretty cheap to compute
and behaves nicely:

![A=-\frac{1}{2}\left(p\cos^2\theta + q\sin^2\theta\right)](https://s0.wp.com/latex.php?latex=A%3D-%5Cfrac%7B1%7D%7B2%7D%5Cleft%28p%5Ccos%5E2%5Ctheta+%2B+q%5Csin%5E2%5Ctheta%5Cright%29&bg=ffffff&fg=000000&s=0 "A=-\frac{1}{2}\left(p\cos^2\theta + q\sin^2\theta\right)")

,

![B=\cos\theta \sin\theta(q-p)](https://s0.wp.com/latex.php?latex=B%3D%5Ccos%5Ctheta+%5Csin%5Ctheta%28q-p%29&bg=ffffff&fg=000000&s=0 "B=\cos\theta \sin\theta(q-p)")

, and

![C=-\frac{1}{2}\left(p\sin^2\theta + q\cos^2\theta\right)](https://s0.wp.com/latex.php?latex=C%3D-%5Cfrac%7B1%7D%7B2%7D%5Cleft%28p%5Csin%5E2%5Ctheta+%2B+q%5Ccos%5E2%5Ctheta%5Cright%29&bg=ffffff&fg=000000&s=0 "C=-\frac{1}{2}\left(p\sin^2\theta + q\cos^2\theta\right)")

. It shouldn’t be hard to see that

![\sigma_1 = p^{-1/2}](https://s0.wp.com/latex.php?latex=%5Csigma_1+%3D+p%5E%7B-1%2F2%7D&bg=ffffff&fg=000000&s=0 "\sigma_1 = p^{-1/2}")

and

![\sigma_2 = q^{-1/2}](https://s0.wp.com/latex.php?latex=%5Csigma_2+%3D+q%5E%7B-1%2F2%7D&bg=ffffff&fg=000000&s=0 "\sigma_2 = q^{-1/2}")

. Here, the optimizer may end up with either of the σ values being the larger.
If σ2 > σ1, you can exchange them and add (or subtract) π/2 to θ.

**Probabalistic.** Change gears for a second. What if we interpret our 2D
Gaussian as expressing the joint behavior of variables x and y, with standard
deviations σx and σy and covariance Cxy? In this case, we still ignore mean
values, but there is one correct normalization:

![p(x,y|\sigma_x,\sigma_y,C_{xy}) = \frac{1}{2\pi\sqrt{\sigma_x^2\sigma_y^2-C_{xy}^2}} \exp(Ax^2 + Bxy + Cy^2),](https://s0.wp.com/latex.php?latex=p%28x%2Cy%7C%5Csigma_x%2C%5Csigma_y%2CC_%7Bxy%7D%29+%3D+%5Cfrac%7B1%7D%7B2%5Cpi%5Csqrt%7B%5Csigma_x%5E2%5Csigma_y%5E2-C_%7Bxy%7D%5E2%7D%7D+%5Cexp%28Ax%5E2+%2B+Bxy+%2B+Cy%5E2%29%2C&bg=ffffff&fg=000000&s=0 "p(x,y|\sigma_x,\sigma_y,C_{xy}) = \frac{1}{2\pi\sqrt{\sigma_x^2\sigma_y^2-C_{xy}^2}} \exp(Ax^2 + Bxy + Cy^2),")

where

![A=-\frac{\sigma_y^2}{2(\sigma_x^2\sigma_y^2-C_{xy}^2)},](https://s0.wp.com/latex.php?latex=A%3D-%5Cfrac%7B%5Csigma_y%5E2%7D%7B2%28%5Csigma_x%5E2%5Csigma_y%5E2-C_%7Bxy%7D%5E2%29%7D%2C&bg=ffffff&fg=000000&s=0 "A=-\frac{\sigma_y^2}{2(\sigma_x^2\sigma_y^2-C_{xy}^2)},")

![B = \frac{C_{xy}}{\sigma_x^2\sigma_y^2-C_{xy}^2},](https://s0.wp.com/latex.php?latex=B+%3D+%5Cfrac%7BC_%7Bxy%7D%7D%7B%5Csigma_x%5E2%5Csigma_y%5E2-C_%7Bxy%7D%5E2%7D%2C&bg=ffffff&fg=000000&s=0 "B = \frac{C_{xy}}{\sigma_x^2\sigma_y^2-C_{xy}^2},")

![C=-\frac{\sigma_x^2}{2(\sigma_x^2\sigma_y^2-C_{xy}^2)}.](https://s0.wp.com/latex.php?latex=C%3D-%5Cfrac%7B%5Csigma_x%5E2%7D%7B2%28%5Csigma_x%5E2%5Csigma_y%5E2-C_%7Bxy%7D%5E2%29%7D.&bg=ffffff&fg=000000&s=0 "C=-\frac{\sigma_x^2}{2(\sigma_x^2\sigma_y^2-C_{xy}^2)}.")

These unpleasant expressions are difficult to invert. If you’re trying to
solve for a covariance matrix from some data, use
[`numpy.cov`](http://docs.scipy.org/doc/numpy/reference/generated/numpy.cov.html)
or read
[Estimation of covariance matrices](http://en.wikipedia.org/wiki/Estimation_of_covariance_matrices).
It is surprising to me how difficult it is to relate σx, σy, and Cxy to other
quantities — everything seems to be done best by going through σ1, σ2, and θ
(see `ellpar` below).

**Alternate numerically-friendly probabalistic.** The numerically-friendly
version above still requires p, q > 0 and is periodic with θ. If the above
probabalistic approach is workable, use

![\sigma_x = e^u](https://s0.wp.com/latex.php?latex=%5Csigma_x+%3D+e%5Eu&bg=ffffff&fg=000000&s=0 "\sigma_x = e^u")

![\sigma_y = e^v](https://s0.wp.com/latex.php?latex=%5Csigma_y+%3D+e%5Ev&bg=ffffff&fg=000000&s=0 "\sigma_y = e^v")

![C_{xy} = e^{u+v}\tanh w](https://s0.wp.com/latex.php?latex=C_%7Bxy%7D+%3D+e%5E%7Bu%2Bv%7D+%5Ctanh+w&bg=ffffff&fg=000000&s=0 "C_{xy} = e^{u+v} \tanh w")

. For initialization,

![w = \mathop{\mathrm{arctanh}} \frac{C_{xy}}{\sigma_x \sigma_y}.](https://s0.wp.com/latex.php?latex=w+%3D+%5Cmathop%7B%5Cmathrm%7Barctanh%7D%7D+%5Cfrac%7BC_%7Bxy%7D%7D%7B%5Csigma_x+%5Csigma_y%7D.&bg=ffffff&fg=000000&s=0 "w = \mathop{\mathrm{arctanh}} \frac{C_{xy}}{\sigma_x \sigma_y}.")

**Wikipedia.** The
[Wikipedia page on Gaussian Functions](http://en.wikipedia.org/wiki/Gaussian_function)
uses:

![z = \exp\left(-\left[ax^2 + 2bxy + cy^2\right]\right)](https://s0.wp.com/latex.php?latex=z+%3D+%5Cexp%5Cleft%28-%5Cleft%5Bax%5E2+%2B+2bxy+%2B+cy%5E2%5Cright%5D%5Cright%29&bg=ffffff&fg=000000&s=0 "z = \exp\left(-\left[ax^2 + 2bxy + cy^2\right]\right)")

Here the condition on the parameters is that the matrix `[a b \ b c]` be
positive definite, or that

![az_1^2 + bz_1z_2 + cz_2^2 > 0\, \forall z_1, z_2](https://s0.wp.com/latex.php?latex=az_1%5E2+%2B+bz_1z_2+%2B+cz_2%5E2+%3E+0%5C%2C+%5Cforall+z_1%2C+z_2&bg=ffffff&fg=000000&s=0 "az_1^2 + bz_1z_2 + cz_2^2 > 0\, \forall z_1, z_2")

(or, equivalently I think, that _a_ and _c_ be positive and _b_² < _ac_).

Wikipedia gives a conversion formula to this system from major/minor/PA, but
there are two caveats: the Wikipedia system names σ{1,2} as σ{x,y} somewhat
misleadingly, and inverts θ to be a _clockwise_ rotation from +x to -y. Avoid
those equations since the ones I give above are clearer.

# Gaussian Convolutions

Resolved sources are often modeled as 2D Gaussians. These are convolved with
the 2D Gaussian of your synthesized beam, so one often wants to compute this
convolution or deconvolution analytically. The file
[`src/subs/gaupar.for`](https://github.com/pkgw/carma-miriad/blob/CVSHEAD/src/subs/gaupar.for)
in MIRIAD has routines for going both directions, and they are not trivial.
The deconvolution case needs special handling for sources that are close to
(or smaller than!) point sources. The existing heuristics seem only so-so. See
[`pwpy/scilib/astutil.py`](https://github.com/pkgw/pwpy/blob/master/scilib/astutil.py)
for a Python deconvolution implementation.

To manage flux through such a deconvolution, work in total
flux units. Nothing changes! The _peak_ flux is scaled in two ways: once, to
convert from Jy/bm to Jy/px (assuming this is what you’re doing), which
involves the beam volume and the pixel volume; and once to convert the source
area, which involves the original volume and the deconvolved volume.

# Gaussian Coordinate Transformations

When you have a Gaussian model for a source, this usally needs to be rendered
into actual pixels or something.

Doing this purely geometrically is difficult. For instance, in a given map
projection, the RA/Dec axes may not be precisely aligned with the X/Y pixel
axes. If you want to draw a Gaussian source as an ellipse, you need to rotate
it a little bit. If the source is very large, these effects change over the
source extent and things get scary. _It’s better to calculate the RA/Dec of
each pixel and brute-force your way through many of these issues._

To do this brute forcing, you need to find the  value of the
parameter that goes in the exponential. You can think of this as computing a
distance in from the origin in the transformed space where the Gaussian is a
circle. You un-translate, then un-rotate, then un-scale:

```python
def gaussdist(x0, y0, maj, min, pa, x, y):
    # x0, y0: Gaussian center
    # maj, min: major/minor axes
    # pa: position angle, from +x toward +y

    dx, dy = x - x0, y - y0
    c, s = np.cos(pa), np.sin(pa)
    a = c * dx + s * dy
    b = -s * dx + c * dy
    d2 = (a / maj)**2 + (b / min)**2

    # d2: squared "distance" from Gaussian such
    # that z = exp(-0.5 * d2)
    return d2
```

The astronomical “East from North” PA
convention means that you can replace _X_ with _declination_ and _Y_ with
_right ascension_. This formulation can be turned into the one in the
[Wikipedia article on Gaussian Function](http://en.wikipedia.org/wiki/Gaussian_function)
but is a lot simpler to think about.

# A: Converting Jy/pixel to Jy/arcsec²

To do this you need to calculate the size
of a pixel at the position of the source you’re considering. Code to do this
is in [`pwpy/intfbin/msimgen`](https://github.com/pkgw/pwpy/blob/master/i
ntfbin/msimgen). It looks something like this:

```python
def pixelvolume(pixel2world, pixelcoords):
    delta = 1e-5
    w1 = pixel2world(pixelcoords)
    pixelcoords[X] += delta
    pixelcoords[Y] += delta
    w2 = pixel2world(pixelcoords)
    dra = w2[RA] - w1[RA]
    ddec = w2[DEC] - w2[DEC]
    return (dra**2 + ddec**2) / (2 * delta**2)
```

# B: Error Ellipses From Covariant Variables

This is almost entirely unrelated
to everything else here, except that it involves 2D Gaussians. Given two
correlated variables, what are the parameters of the ellipse that describes a
confidence region?

```python
def ellpar(sx, sy, cxy):
    # sx: std dev (not variance) of x var
    # sy: std dev (not variance) of y var
    # cxy: covariance (not corr. coeff.) of x and y

    from numpy import arctan2, sqrt

    pa = 0.5 * arctan2(2 * cxy, sx**2 - sy**2)
    h = sqrt((sx**2 - sy**2)**2 + 4*cxy**2)  
    maj = sqrt(2 * (sx**2 * sy**2 - cxy**2) / (sx**2 + sy**2 - h))
    min = sqrt(2 * (sx**2 * sy**2 - cxy**2) / (sx**2 + sy**2 + h))

    # maj/min: major/minor axes of ellipse
    # note: sigmas, not FWHMs
    # pa: position angle of ellipse, rotating from +x to +y
    return maj, min, pa
```

Say we want to draw an actual ellipse representing this bivariate
distribution, so that the area within the ellipse represents a certain
confidence interval on predicted values. Parametrize this with a value f(CL),
where we draw an ellipse that has axes of sizes f*maj and f*min. By
transforming X and Y to have a mean of 0 and stddev of 1, then considering the
probability distribution of r = x²+y², we can find the relationship between
the axis lengths and the confidence interval they subsume. P(r) = r exp
(-r²/2) so

![f(\textrm{CL}) = \sqrt{-2 \ln (1-\textrm{CL})}.](https://s0.wp.com/latex.php?latex=f%28%5Ctextrm%7BCL%7D%29+%3D+%5Csqrt%7B-2+%5Cln%281-%5Ctextrm%7BCL%7D%29%7D.&bg=ffffff&fg=000000&s=0 "f(\textrm{CL}) = \sqrt{-2 \ln(1-\textrm{CL})}.")

We see that if we just draw the ellipse according to values associated with
the underlying distribution, we get the 39% confidence interval. If we want
one in terms of the usual σ limits, we must scale by

![f(\sigma) = \sqrt{-2 \ln \mathop{\mathrm{erfc}} (\f rac{\sigma}{\sqrt{2}})}.](https://s0.wp.com/latex.php?latex=f%28%5Csigma%29+%3D+%5Csqrt%7B-2+%5Cln+%5Cmathop%7B%5Cmathrm%7Berfc%7D%7D+%28%5Cfrac%7B%5Csigma%7D%7B%5Csqrt%7B2%7D%7D%29%7D.&bg=ffffff&fg=000000&s=0 "f(\sigma) = \sqrt{-2\ln \mathop{\mathrm{erfc}} (\frac{\sigma}{\sqrt{2}})}.")

For 1 sigma this about 1.5 and for 2 sigma it’s about 2.5. **Note:** Earlier I
had this analysis all wrong!

# C: Tracing Ellipses

To trace an
ellipse, all we need to do is express it in parametric form. Let `th` be an
offset angle from the major axis of the ellipse. In code form:

```python
def ellpoint(th, x0, y0, maj, min, pa):
    from numpy import cos, sin

    x = x0 + maj * cos(th) * cos(pa) - min * sin(th) * sin(pa)
    y = y0 + maj * cos(th) * sin(pa) + min * sin(th) * cos(pa)
    return x, y
```

That’s all there is to it.
