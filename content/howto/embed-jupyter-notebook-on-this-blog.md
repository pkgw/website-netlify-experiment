+++
date = 2014-08-04T00:00:00-04:00
title = "Embed a Jupyter Notebook on this Blog"
weight = 0 # all howtos have zero weight => alphabetical ordering
template = "howto.html"
+++

*Warning:* these instructions are old and need revision.

1. Write up the notebook. Make sure to keep lines short since there isn’t
   much horizontal room in the blog format.
2. Run:
   ```sh
   ipython nbconvert --to html notebook.ipynb
   ```
3. Copy the output file to a name like `notebook-title.html`.
4. Add tweaks at the end of the CSS, just before the “Custom stylesheet” comment:
   ```css
   img { max-width: 560px !important: } /* TO BE CONFIRMED */
   .prompt { display: none; }
   body { padding: 0; }
   div.text_cell_render { padding: 0; }
   ```
   Font matching is difficult because you can’t bridge CSS *et al* in iframes,
   and the outer level has its own magic setup.
5. Use Gutenberg’s colocated assets to include the notebook HTML, and embed a
   link emulating
   [this example](https://github.com/pkgw/website/blob/master/content/2014/elementary-gaussian-processes-in-python.md).
