+++
date = 2019-07-23T01:36:06-04:00
title = "Fix broken conda(-forge) compilers on MacOS"
weight = 0 # all howtos have zero weight => alphabetical ordering
template = "howto.html"
+++

I got stuck on this error for a long time:

```
ld: library not found for -lSystem
```

In the end, it turned out that the `conda-build` system was setting
`$CONDA_BUILD_SYSROOT` to `/opt/MacOSX10.10.sdk`, which was a path that did
not exist on my machine. I can't figure out where exactly the setting
gets injected.

There may be a way to override it, but I thought it was easier just to
make a symlink to that path. This command prints the sysroot for the
main XCode install:

```
xcrun --show-sdk-path
```

Which may yield a result something like
`/Applications/XCode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.12.sdk`.

See also
[conda-forge/conda-forge.github.io#824](https://github.com/conda-forge/conda-forge.github.io/issues/824).
