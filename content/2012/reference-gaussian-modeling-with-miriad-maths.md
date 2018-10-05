+++
date = 2012-04-17T14:08:37Z
title = "Reference: Gaussian Modeling with MIRIAD maths"

[extra]
wp_rel_permalink = "/2012/04/reference-gaussian-modeling-with-miriad-maths/"
wp_shortlink = "/?p=542"
+++

A note to self. Sometimes I want to use `maths` to generate an image with a
large Gaussian component. Let’s say that the total flux I want to capture is F
(in Janskys). Using what we know about normalized Gaussians the expression I
want is something of the form

![\frac{F}{2\pi\sigma_x\sigma_y} \exp\left(-\frac{1}{2}\left[\frac{x^2}{\sigma_x^2}+\frac{y^2}{\sigma_y^2}\right]\right)](https://s0.wp.com/latex.php?latex=%5Cfrac%7BF%7D%7B2%5Cpi%5Csigma_x%5Csigma_y%7D+%5Cexp%5Cleft%28-%5Cfrac%7B1%7D%7B2%7D%5Cleft%5B%5Cfrac%7Bx%5E2%7D%7B%5Csigma_x%5E2%7D%2B%5Cfrac%7By%5E2%7D%7B%5Csigma_y%5E2%7D%5Cright%5D%5Cright%29&bg=ffffff&fg=000000&s=0 "\frac{F}{2\pi\sigma_x\sigma_y} \exp\left(-\frac{1}{2}\left[\frac{x^2}{\sigma_x^2}+\frac{y^2}{\sigma_y^2}\right]\right)")

. Assuming circularity and simplifying, we get

![A\exp\left(B\left[x^2+y^2\right]\right)](https://s0.wp.com/latex.php?latex=A%5Cexp%5Cleft%28B%5Cleft%5Bx%5E2%2By%5E2%5Cright%5D%5Cright%29&bg=ffffff&fg=000000&s=0"A\exp\left(B\left[x^2+y^2\right]\right)")

, where

![A = \frac{F}{2\pi\sigma^2}](https://s0.wp.com/latex.php?latex=A+%3D+%5Cfrac%7BF%7D%7B2%5Cpi%5Csigma%5E2%7D&bg=ffffff&fg=000000&s=0 "A = \frac{F}{2\pi\sigma^2}")

and

![B=-\frac{1}{2\sigma^2}](https://s0.wp.com/latex.php?latex=B%3D-%5Cfrac%7B1%7D%7B2%5Csigma%5E2%7D&bg=ffffff&fg=000000&s=0 "B=-\frac{1}{2\sigma^2}")

.

For now I’ve thought through the implementation using arcsecond units. Say we
have a 2047×2047 image with a pixel scale of 10 arcsec that’s uniform across
the image. If I want σ to measure the ATA primary beam, with a FWHM of
3.5°/GHz, I get σ = 5350.7 arcsec/GHz. _To generate a model-type image, we
need to work in Jy/pixel_, so A must be scaled by the arcsec²/pixel conversion
ratio, 100 in this case.

Implementing this in `maths` is straightforward. You use the `xrange` and
`yrange` keywords to implement the Gaussian expression, ranging them from
-10230 to +10230 in the example here.
