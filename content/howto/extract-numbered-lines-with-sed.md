+++
date = 2015-09-22T00:00:00-04:00
title = "Extract Numbered Lines from a File with sed"
weight = 0 # all howtos have zero weight => alphabetical ordering
template = "howto.html"
+++

Easy if you can ever remember the magic syntax:

```sh
sed -e 'AAA,BBB!d' file.txt
```

… where AAA and BBB are 1-based line numbers, and the range is treated
inclusively.
