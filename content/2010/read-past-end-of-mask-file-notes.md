+++
date = 2010-06-10T13:58:59Z
title = "“Read past end of mask file” Notes"
path = "2010/06/read-past-end-of-mask-file-notes"

[extra]
wp_rel_permalink = "/2010/06/read-past-end-of-mask-file-notes/"
wp_shortlink = "/?p=219"
+++

More boring reference material! This time, certain ATA datasets are rejected
by MIRIAD with a “Read past end of mask file” error. These datasets are almost
entirely good, and fixable, so it’s a shame to discard them.

**Example.** See

```
/ataarchive/2010/03/11/gcs/d1cb41d2/s000
```

**Diagnosis.** As one might guess: there are more visibility records than
there are flags. So far, it seems to be the case that only the flags for the
very final UV record are missing. This appears to be caused by killing the
datacatcher instead of leaving it to shutdown on its own volition.

**Detection.** Run itemize on the dataset:

```
itemize: CVS Version 1.6, 2009/10/27 02:55:56 UTC
  npol     = 4
  obstype  = mixed-auto-cross
  nwcorr   = 0
  ncorr    = 8897536
  vislen   = 36202896
  history    (text data, 10834 elements)
  flags     (integer data, 286985 elements)
  vartable   (text data, 430 elements)
  c_tstop    (text data, 38 elements)
  c_instr    (text data, 30 elements)
  visdata    (binary data, 36202896 elements)
```

Each dword “element” in the flags record has 31 bits used for flag
information, except for the very last one, which may be padded out with junk
data. So, let `X = <ncorr> – <# flag elements> * 31`. If X is between 0 and
-30, inclusively, we have a valid dataset. If X is between 994 and 1024,
inclusively, we have an invalid dataset that is missing its final record
(assuming 1024 channels of course). If neither of these holds, we have
something weird going on.

Instead of using “itemize” to get the number of flag data, you can use the
file size. There’s 31 bits per four bytes and a header dword, so the
expression is `31 * (<flags file size in bytes> / 4 – 1)`.

**Correction.** I wrote a program to do it. See

```
viskit/demo/ataflagfix.c
```
