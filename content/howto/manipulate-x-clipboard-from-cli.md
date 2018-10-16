+++
date = 2015-11-07T00:00:00-04:00
title = "Manipulate the X Clipboard from the Command Line"
weight = 0 # all howtos have zero weight => alphabetical ordering
template = "howto.html"
+++

The key is the [xclip](https://github.com/astrand/xclip) program! To put text
into the X clipboard (“copy”):

```sh
xclip -b <file.txt
```

To fetch the text from the X clipboard (“paste”):

```sh
xclip -b -o >file.txt
```

On Fedora, this requires installing the `xsel` package.
