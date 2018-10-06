+++
date = 2010-12-19T23:19:31Z
title = "Reference: CSS image too tall for its text"
path = "2010/12/reference-css-image-too-tall-for-its-text"

[extra]
wp_rel_permalink = "/2010/12/reference-css-image-too-tall-for-its-text/"
wp_shortlink = "/?p=379"
+++

A technical note-to-self on a problem that I’ve run into a few times.
Sometimes when setting up webpages, one wants to have a box with some kind of
graphic floated to the side of some text. Because the graphic is floated, it
apparently doesn’t affect the height of the whole box, so if the text is too
short, the box is shorter than the graphic and looks terrible.

The solution — or, a solution that at least works in Firefox — is to add an
empty element with its CSS “clear” property set to “both” at the bottom of the
box. The “clear” property forces the element to be laid out below any floats,
which extends the height of the non-floating material to be sufficiently tall.
This is easy to do with:

```
<div style="clear: both;"></div>
```

after the text and image elements.
