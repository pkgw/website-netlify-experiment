+++
date = 2018-09-03T00:00:00-04:00
title = "Fix Mysteriously Dying Windows Programs"
weight = 0 # all howtos have zero weight => alphabetical ordering
template = "howto.html"
+++

(… in certain circumstances, at least.)

*Symptom:* a program seems to compile fine, but dies when run. No visible
 error message on the console, but the exit code is -1073741515.

*Cause*: MSVC install sometimes fails to install `ucrtbased.dll` in the right
place! Most common solution on the internet is “uninstall and reinstall Visual
Studio a few times until it appears”. WTF.

*Workaround*: Pretty sure this works:

```
copy "C:\Program Files (x86)\Windows Kits\10\bin\x64\ucrt\ucrtbased.dll"
  "C:\Windows\System32"
```

Although as far as I can tell, this is not an encouraged approach (surprise).

(Originally posted
[on Tumblr](http://pkgw.tumblr.com/post/177716510051/absolutely-bananas-msvc-problem.)
