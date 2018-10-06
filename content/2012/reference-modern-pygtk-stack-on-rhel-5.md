+++
date = 2012-11-20T10:35:34Z
title = "Reference: Modern pyGTK+ stack on RHEL 5"
path = "2012/11/reference-modern-pygtk-stack-on-rhel-5"

[extra]
wp_rel_permalink = "/2012/11/reference-modern-pygtk-stack-on-rhel-5/"
wp_shortlink = "/?p=613"
+++

Certain software projects like to target “enterprise”-class Linux
distributions that have super old versions of certain key pieces of software.
If, for instance, you want to actually use a somewhat modern GTK+ from Python,
here’s the ordered list of dependencies that you’ll need to install:

1. Python >= 2.6. (Versus the 2004-vintage Python 2.4 that comes by default on
   RHEL 5.) CASA bundles
   [Python 2.6.5](http://www.python.org/ftp/python/2.6.5/Python-2.6.5.tar.bz2)
   and you need to use its Python to get its special libraries, so use that.

2. [libffi 3.0.11](ftp://sourceware.org/pub/libffi/libffi-3.0.11.tar.gz)

3. [glib 2.34.2](http://ftp.gnome.org/pub/gnome/sources/glib/2.34/glib-2.34.2.tar.xz)

4. [pixman 0.28.0](http://cairographics.org/releases/pixman-0.28.0.tar.gz)

5. [cairo 1.12.6](http://cairographics.org/releases/cairo-1.12.6.tar.xz)

6. [gobject-introspection 1.34.2](http://ftp.gnome.org/pub/gnome/sources/gobject-introspection/1.34/gobject-introspection-1.34.2.tar.xz)

7. [gdk-pixbuf 2.26.5](http://ftp.gnome.org/pub/gnome/sources/gdk-pixbuf/2.26/gdk-pixbuf-2.26.5.tar.xz)

8. [freetype 2.4.10](http://download.savannah.gnu.org/releases/freetype/freetype-2.4.10.tar.bz2)

9. [harfbuzz 0.9.6](http://www.freedesktop.org/software/harfbuzz/release/harfbuzz-0.9.6.tar.bz2)

10. [fontconfig 2.10.1](http://www.freedesktop.org/software/fontconfig/release/fontconfig-2.10.1.tar.bz2)

11. [pango 1.32.2](http://ftp.acc.umu.se/pub/gnome/sources/pango/1.32/pango-1.32.2.tar.xz)

12. [atk 2.6.0](http://ftp.gnome.org/pub/gnome/sources/atk/2.6/atk-2.6.0.tar.xz)

13. [gtk+ 2.24.13](http://ftp.gnome.org/pub/gnome/sources/gtk+/2.24/gtk+-2.24.13.tar.xz)

14. [pygobject 2.28.6](http://ftp.gnome.org/pub/gnome/sources/pygobject/2.28/pygobject-2.28.6.tar.xz)
    with
    [this patch](http://mail-index.netbsd.org/pkgsrc-users/2012/02/08/msg015675.html)
    and [this optional one](/wp/wp-content/uploads/2014/03/gobj-warn.diff)

15. [py2cairo 1.10.0](http://www.cairographics.org/releases/py2cairo-1.10.0.tar.bz2)
    — uses “waf” build tool that may require the futzing mentioned
    [at the end of this thread](https://groups.google.com/forum/?fromgroups=#!topic/waf-users/8Xt4BbxM6i8)

16. [pygtk 2.24.0](http://ftp.gnome.org/pub/gnome/sources/pygtk/2.24/pygtk-2.24.0.tar.bz2)

Obviously, somewhat different versions are probably OK, though too-new stuff
probably targets Python 3 and GTK+ 3 and opens a huge can of worms if your
code is targeting version 2 of each of those.

Building everything is tedious but not generally difficult, though there isn’t
much documentation about how to pass extra info to `waf` if it can’t guess the
right flags for things.
