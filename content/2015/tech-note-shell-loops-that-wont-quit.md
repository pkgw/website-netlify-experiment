+++
date = 2015-01-16T19:44:19Z
title = "Tech note: shell loops that won’t quit"

[extra]
wp_rel_permalink = "/2015/01/tech-note-shell-loops-that-wont-quit/"
wp_shortlink = "/?p=918"
+++

For a long time, I’ve noticed that _sometimes_ my shell scripts that use loops
behave funny. Normally, when you hit control-C to cancel a script in the
middle of a loop, the whole thing just exits. But in some cases I found that
the control-C would cancel the current program, but not the whole script. This
gets annoying if your loop is running time-consuming processing on hundreds of
data sets — you have to sit there hitting control-C over and over again.

After a lot of detective work, I finally figured out what was going on. Here’s
a clue. You can control-C this shell script and it will exit as expected:

```sh
for i in 1 2 3 4 5 ; do
  echo $i
  /usr/bin/sleep 10
done
```

But this one won’t:

```sh
for i in 1 2 3 4 5 ; do
  echo $i
  python -c "import time; time.sleep(10)"
done
```

What the heck is Python up to? As you’d expect, I found a lot of
misinformation online, but unexpectedly, I’ve barely been able to dig up _any_
relevant and correct information. Fortunately, I finally found
[this article by Martin Cracauer](http://www.cons.org/cracauer/sigint.html),
which set me straight.

Imagine that a shell script is running a long-running subprogram. When you hit
control-C, both of the programs receive a
[SIGINT](http://en.wikipedia.org/wiki/Unix_signal#SIGINT) signal. In most
cases the subprogram dies immediately. However, the shell’s behavior needs to
be more complicated, because some subprograms handle the SIGINT and _don’t_
die. The shell needs to wait and see what happens to the subprogram: it
shouldn’t kill itself if the subprogram didn’t. The shell implements this
logic by waiting for the subprogram to exit and using POSIX-defined macros
like
[WIFSIGNALED](http://pubs.opengroup.org/onlinepubs/9699919799/functions/wait.html)
to test how it died; specifically,
[if it got killed by a SIGINT or exited for some other
reason](http://git.savannah.gnu.org/cgit/bash.git/tree/jobs.c#n3273).

If you’re familiar with Python, you might see the contours of the problem.
Python catches SIGINT and turns it into a
[KeyboardInterrupt](https://docs.python.org/2/library/exceptions.html#exceptions.KeyboardInterrupt) exception, which your
code can then handle. However, it turns out that if you don’t handle it,
Python exits through its normal means, effectively using
[sys.exit](https://docs.python.org/2/library/sys.html#sys.exit) with an error
code. In other words, from the shell’s perspective the subprogram _doesn’t_
get killed by the SIGINT, and so then the shell decides that it shouldn’t give
up either.

If you want to convince the shell that you _did_ die from SIGINT, you can’t
fake it with a special exit code or anything. You have to _kill yourself_ with
an honest-to-goodness SIGINT signal. Fortunately,
[it’s not hard to do that](https://github.com/pkgw/pwkit/blob/master/pwkit/cli/__init__.py#L120).
I’d say this is a bug in Python: uncaught KeyboadInterrupts should lead to the
process killing itself this way.

Once I figured out what was going on, it was easy to code up a fix that works
by intercepting
[sys.excepthook](https://docs.python.org/2/library/sys.html#sys.excepthook).
I’ve
[added it](https://github.com/pkgw/pwkit/commit/c9fa0b3b5685c9c7590e32f7dc18e648ac72f844)
to my [pwkit](https://github.com/pkgw/pwkit/) package, which includes several
utilities useful for writing Python programs that operate on the command line,
including a progam called
[wrapout](https://github.com/pkgw/pwkit/blob/master/pwkit/cli/wrapout.py) that
I’ve found to be very useful.

And yes, the fix totally works. I’m sure that other sets of software suffer
from the same issue, and it’s unfortunate that you have to explicitly enable
the fix in Python. (I checked and this is true for Python 3 as well as Python
2.) But if you were ever befuddled about what was going on, now you know!

(Oh, by the way: nothing about this is specific to loops at all. They just
expose the problem in the most obvious way.)
