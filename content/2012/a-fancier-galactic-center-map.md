+++
date = 2012-02-17T21:50:57Z
title = "A Fancier Galactic Center Map"
path = "2012/02/a-fancier-galactic-center-map"

[extra]
wp_rel_permalink = "/2012/02/a-fancier-galactic-center-map/"
wp_shortlink = "/?p=506"
+++

Here’s another version of the ATA map of the Galactic Center
[that I posted earlier](./2011/the-galactic-center-as-seen-by-the-ata.md). The
data are completely the same; I’ve just put together all of the pieces to be
able to render the map into a pretty, correct PDF. 
{{ulink(path="wp/wp-content/uploads/2012/02/gpmos.pdf", text="Tadaa!")}}

{% figure(src="/~peter/wp/wp-content/uploads/2012/02/gpmos.png") %}
This is just a preview! The real image is a PDF.
{% end %}

Look at how nice and text-selectable the labels are. Appreciate the lovely,
colorblind-person-friendly colorization. Ponder the honoring of the image
mask. Marvel at the lack of resampling of the underlying image data!

The only deficiencies that come to _my_ mind are the excessively large margins
and the lack of a synthesized beam size indicator. I had to wrestle with some
unpleasant implementation details to get it all to work though.
[Like this](https://github.com/pkgw/omegaplot/commit/34f7b348929693a989339c5a1c64c9da5c37a620).
Time to call it a day.
