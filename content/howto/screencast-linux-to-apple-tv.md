+++
date = 2015-02-24T00:00:00-04:00
title = "Screencast from Linux to Apple TV"
weight = 0 # all howtos have zero weight => alphabetical ordering
template = "howto.html"
+++

Such screencasting happens over the AirPlay protocol. The Linux box is then
the AirPlay sender, of course. This shouldn’t be hard since Apple wants to
make it easy for people to show stuff on Apple TVs! If weird embedded devices
can do it, Linux should be able to too.

I used [this jar](https://github.com/jamesdlow/open-airplay/releases) (plus
[this one](https://github.com/jamesdlow/open-airplay/blob/master/Java/lib/jmdns.jar))
and it worked OK. You can’t combine the `-classPath` and `-jar` options to
Java (??) so I had to run:

```sh
java -cp 'jmdns.jar:airplay.jar' com.jameslow.AirPlay
```

which took a little bit of time but more or less worked. Couldn’t see mouse
cursor, window management was a litle wonky, etc. I feel like I should be able
to find something that works at least a bit better.
