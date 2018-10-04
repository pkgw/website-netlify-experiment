+++
date = 2013-07-27T13:17:35Z
title = "Fixing erroneous “Insufficient storage available” errors on Android"

[extra]
wp_rel_permalink = "/2013/07/fixing-erroneous-insufficient-storage-available-errors-on-android/"
wp_shortlink = "/?p=750"
+++

**Short answer:** the fix _might_ be to delete `/data/app-lib/APP-PATH/lib`.
You need root.  What better way to spend a sunny morning than fixing problems
with my phone?  For a while, I’ve had problems on my Nexus 4 where certain
apps would refuse to install, or I couldn’t update them once they were
installed. The error message would be “Insufficient storage available,” but
that was clearly wrong because I had plenty of storage space available and the
apps were small.  Now, most technical problems are best addressed with
thorough Googling, but this kind of problem is a toughie. Amateur-hour Android
phone futzing is a fascinating corner of the internet in its way — grounds for
a dissertation in cargo cult behavior. Between poor reading comprehension
(“try moving your apps to the SD card!”), lack of actual knowledge of how the
system works (“I dunno, try clearing all of your app data?”) and excessive
leverage (“try upgrading your CyanogenMod hacked ROM to the latest version and
running \[root\]CacheCleaner-v7.x”), there’s a lot of light but very little
heat.  To be fair, one of the issues is that this kind of error message
apparently has many root causes. My impression is that if anything goes wrong
during an app install, you’ll get the “Insufficient storage available” error.
In the end, the root cause of the error seems to almost always be a leftover
file that somehow interferes with the intended install/update. For instance,
for many people the problem seems to be leftover `.odex` files in `/data/app
([e.g.](http://forum.xda-developers.com/showthread.php?t=1810294)).` For me,
the problem turned out to be strange dangling files in `/data/app-lib`. In
both of the cases I had to deal with, there was a recursive symlink named
`/data/app-lib/APP-PATH/lib`, and blowing away that file solved the problem.
(Here APP-PATH is something like `com.fsck.k9-1` for K9 Mail. Hypothetically.)
I could imagine that in other cases you might need to blow away the whole
`/data/app-lib/APP-PATH` directory ([cf.](http://forum.xda-
developers.com/showthread.php?p=39362544))  The lame thing is that **you need
a rooted phone to do this** — the relevant files are system files. If leftover
`app-lib` files are causing your install/update problems and you _don’t_ have
a rooted phone, I think you’re just sunk. Which makes this a pretty bad bug.
Maybe an OS update will prevent this from happening at some point; if not,
maybe there’s a way to convince the OS to delete the offending directories on
your behalf. Hopefully a fix that works on stock phones will come along,
because this problem seems to bite a lot of people.
