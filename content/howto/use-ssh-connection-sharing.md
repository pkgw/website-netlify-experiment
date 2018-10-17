+++
date = 2013-02-08T00:19:15Z
title = "Use SSH Connection Sharing"
aliases = ["2013/02/fun-with-ssh-configuration-connection-sharing"]
weight = 0 # all howtos have zero weight => alphabetical ordering
template = "howto.html"

[extra]
wp_rel_permalink = "/2013/02/fun-with-ssh-configuration-connection-sharing/"
wp_shortlink = "/?p=647"
+++

This guide describes how to use the “connection sharing” feature of
[OpenSSH](https://www.openssh.com/), the Secure Shell tool that nearly all
scientists use. It is a *super* useful feature but many people don’t know how
to set it up.

# Motivation

More and more organizations are banning
[SSH public-key authentication](https://www.ssh.com/ssh/public-key-authentication)
to their networks, forcing you type in your password for every login. This is
safe, but inconvenient: I’ve found that when I’m running commands on a remote
machine, I can work *much* more smoothly with lots of quick short-lived SSH
sessions rather than having to use one long-lived one.

The “connection sharing” feature of OpenSSH lets you get the benefit of
quickie SSH logins even when every new login requires a typed password.

When connection sharing is activate, the first connection you open to a server
proceeds as normal. However, when you open *additional* connections to a
server, the software will piggyback the new connection over the old one,
*reusing the authentication* — so you won’t have to type your password again.

An important use-case is when you have a program that needs to do something
over SSH. If each SSH connection requires a human to type a password, there’s
no way to automate the execution of your program (e.g., so that it can run in
the background as a [cronjob](https://en.wikipedia.org/wiki/Cron)). But if you
can open a “master” connection that lives indefinitely, your program can do
its SSH business without needing human input. Suddenly you can automate it!

For human-centric activities, connection sharing opens up a convenient
workflow: at the beginning of the day, open up a master connection to your
login node. Hide it in the corner of your screen. Then for the rest of the
day, you can open quick, short SSH connections without the drag of constantly
having to authenticate. Even better, I wrote a program called
[stund](https://github.com/pkgw/stund/) that can open your “master” connection
and completely detach it from your desktop. This might sound small, but I find
that it makes a *surprisingly large* positive difference in how I interact
with remote machines.

Finally, when connection sharing is active, you can do neat stuff like
dynamically open and close port forwards that tunnel over your connection.
This can be great for Jupyter notebooks and the like.


# Setting It Up

The best part about connection sharing is that it’s super easy to set up. Just
put the following lines in the file `~/.ssh/config`:

```
ControlMaster = auto
ControlPath = ~/.ssh/connshare.%C.sock
ControlPersist = no
```

If these lines cause problems, try this alternative:

```
ControlMaster = auto
ControlPath = ~/.ssh/connshare.%h_%p_%r.sock
```

(This variation has a better chance of working with older versions of
OpenSSH.) You can read the
[`ssh_config`](http://www.manpagez.com/man/5/ssh_config/) manpage to learn
about the meaning of these settings and what some possible alternatives are.

With this setup, you can log in once at the beginning of the day and not worry
about typing your password until quittin’ time, if you don’t close the
original session.


# While I’m At It …

Here a few other SSH tips:

- If you log in to remote computers a lot, the _single biggest_ favor you can
  do yourself is to learn how to use
  [screen](http://www.gnu.org/software/screen/) or
  [tmux](https://github.com/tmux/tmux).

- Despite the lack of good introductory materials, it’s also really worthwhile
  to learn how public-key authentication works, and to use SSH keys when
  appropriate.

- … and a super useful thing about SSH keys is the `ssh-agent` program, which
  remembers your decrypted keys. This lets you skip passphrase entry without
  compromising security (at least by real-world standards).

- You may know that `ssh user@host command` will run `command` on your
  destination. To chain SSH invocations, use `ssh -t user@outerhost ssh -t
  innerhost`. The `-t` option is needed for unimportant reasons related to
  password entry.

- Finally, you can also use your `~/.ssh/config` file to preset usernames,
  ports, X11 forwarding, _etc._ for specific hosts. See the
  [manual page](http://www.manpagez.com/man/5/ssh_config/).
