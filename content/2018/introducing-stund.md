+++
date = 2018-10-23T12:15:17-04:00
title = "Introducing stund"
+++

Here’s another bit of backlog to clear out: I’ve been toying with the idea of
writing a certain small utility program for a while now, and earlier this year
I finally want ahead and did it. The result is called
[stund](https://github.com/pkgw/stund/), which is short for “SSH tunnel
daemon”.

<!-- more -->

*stund* will open an SSH tunnel for you and maintain it in the background. The
key trick is that it can do this even when you need to perform some kind of
interactive login to start your connection. This
[UX](https://en.wikipedia.org/wiki/User_experience) might sound simple enough,
but the implementation is surprisingly complex — the only way to accomplish it
is to start SSH attached to its own
[pseudoterminal](https://en.wikipedia.org/wiki/Pseudoterminal), then relay
input back and forth between the user’s terminal and the SSH virtual session
during the login phase.

If you [use SSH connection sharing](@/howto/use-ssh-connection-sharing.md) —
which you should — *stund* makes it so that you can just login once in the
morning and not worry about having to type your password throughout the day.
I’ve found this to be an extremely helpful feature since system administrators
are tending to require password and/or two-factor authentication more and more
these days.

So, yes, the effect is basically like running SSH inside
[screen](https://www.gnu.org/software/screen/), or launching it with
`ControlPersist` set to `yes`. But the user experience is cleaner:

```sh
$ stund open ssh.aoc.nrao.edu
pwilliam@ssh.aoc.nrao.edu’s password:
[Tunnel successfully opened.]
$
```

Importantly, this behavior makes it relatively easy to incorporate *stund*
into shell scripts and other batch-y operations — you can put it at the top of
the file, then use the connection throughout your script. The user can type
their password right off the bat and then walk away. I don’t know how to do
this cleanly with *screen*.

There are more details [in the README](https://github.com/pkgw/stund#readme).
As mentioned in my
[how-to on SSH connection sharing](@/howto/use-ssh-connection-sharing.md),
this kind of user experience polish might not sound important, but I’ve found
that it dramatically smoothes the ways in which I interact with remote
computer systems.

*stund* is a simple static [Rust](https://rust-lang.org/) program, so it
should be pretty easy to install — you will need the Rust compilers, but
they’re [easy to install](https://rustup.rs/) on just about any platform.
*stund* won’t work on Windows, though, because the whole concept of a
pseudoterminal is Unix-specific.
