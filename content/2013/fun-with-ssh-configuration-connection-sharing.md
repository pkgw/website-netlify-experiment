+++
date = 2013-02-08T00:19:15Z
title = "Fun with SSH configuration: connection sharing"
path = "2013/02/fun-with-ssh-configuration-connection-sharing"

[extra]
wp_rel_permalink = "/2013/02/fun-with-ssh-configuration-connection-sharing/"
wp_shortlink = "/?p=647"
+++

Because nothing says “fun” like SSH tricks!

More and more organizations that use SSH are restricting it through “login”
(aka “bastion”) hosts: locked-down machines that are the only bridge between
the wilds of the Internet and internal networks. These often ban
[SSH public-key authentication](https://www.ssh.com/ssh/public-key-authentication),
making you type in your password for every login. This can get to be a hassle
if you’re frequently logging into your internal network. (As a side note, the
link above is to the best explanation I could find, but I imagine it’d still
be confusing for a newbie. Someone needs to write clear pedagogical material
on SSH
with [public keys](http://en.wikipedia.org/wiki/Public-key_cryptography)!)

There’s a somewhat-new feature in OpenSSH that can make life easier, though.
You can now configure it to automatically “share” preexisting connections: if
you’ve got one connection going and try to start another one, it’ll reuse the
authentication and set up the connection without needing a password. So if you
keep your first connection going, you can open more of them for free. Clearly
this won’t always be useful, but for me, it often is.

To set this up, put something like the following lines in `~/.ssh/config`:

```
ControlMaster = auto
ControlPath = ~/.ssh/connshare.%h\_%p\_%r.sock
ControlPersist = no
```

Read the [`ssh_config`](http://www.manpagez.com/man/5/ssh_config/) manpage to
learn about the meaning of these settings and what some possible alternatives
are. Some versions of SSH don’t support the `ControlPersist` option, in which
case you can just leave it out.

With this setup, you can log in once at the beginning of the day and not worry
about typing your password until quittin’ time, if you don’t close the
original session. Or, if you have a program that needs to operate over SSH but
for some reason can’t deal with the password prompts, you can pre-authenticate
the connection and skip them.

While I’m at it, a few other SSH tips:

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
