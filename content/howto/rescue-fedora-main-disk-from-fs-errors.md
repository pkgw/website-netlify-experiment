+++
date = 2014-08-04T00:00:00-04:00
title = "Rescue the Main Disk Partition of a Fedora Machine from Filesystem Errors"
weight = 0 # all howtos have zero weight => alphabetical ordering
template = "howto.html"
+++

(Hard part from [Krzysztof Adamski](http://k.japko.eu/fedora-fsck-root.html).)

First cut: boot with `fsck.mode=force`.

Rescue-mode bootup still mounts all the filesystems, so you can’t `fsck` the
root partition if it’s horked.

Edit the boot parameters and add `rd.break=pre-mount`. This drops you into a
shell before things get mounted.

(Orginally posted
[on Tumblr](http://pkgw.tumblr.com/post/93798712326/rescuing-main-disk-partition-in-fedora-from).)
