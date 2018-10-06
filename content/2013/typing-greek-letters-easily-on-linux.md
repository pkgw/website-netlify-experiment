+++
date = 2013-04-19T15:52:10Z
title = "Typing Greek Letters Easily on Linux"
path = "2013/04/typing-greek-letters-easily-on-linux"

[extra]
wp_rel_permalink = "/2013/04/typing-greek-letters-easily-on-linux/"
wp_shortlink = "/?p=669"
+++

I’ve already written about
[easily entering special characters on Linux](https://newton.cx/~peter/2010/10/fun-with-unicode/)
using the “Compose Key”. The only inconvenient thing about this setup was
entering Greek letters — they’re not included in the default list of
compositions. I’ve learned a few of the raw Unicode values (`Ctrl-Shift-u 0 3
c 3` for σ) but that’s not exactly ideal.

**Disclaimer:** the following _really_ doesn’t work on Fedora 19. I’ve now set
things up with a Greek keyboard option, so that hitting Super-Space once will
switch me to Greek letters, and hitting it again will bring me back to normal.
No more thin nonbreaking space or blackboard bold for me, though. Annoying.

You can customize the composition list to include things like Greek letters,
with some limitations. Here’s the recipe for Gnome 3 on Fedora:

- Copy the default mapping file, `/usr/share/X11/locale/en_US.UTF-8/Compose`,
  to `~/.XCompose`.

- Edit the file to include your new mappings — the format should be obvious.
  [Here are my new entries](https://gist.github.com/pkgw/5422749) that add
  Greek letters (γαγ), math blackboard bold capitals, and the
  [thin nonbreaking space](http://en.wikipedia.org/wiki/Nonbreaking_space). I
  prefixed the Greek alphabet with “g”, so that `Compose-g-b` gives β.

- You must be using the `xim` input method for the file to take effect. On my
  current Gnome/Fedora setup, I just had to run the “Input Method Selector”
  program and choose “Use X Compose table” from the list of options.

That’s more or less it. However, the settings don’t get applied consistently —
there seems to be a conflict between the way that the Gnome Shell wants to do
input and this customization. If you start a program from the terminal, custom
settings seem to take effect, but if you launch it from the Shell directly,
they might not. I haven’t yet found a way to get everything on the same page.

**Hack:** after login, run

```sh
imsettings-reload
gnome-shell --replace &
```

in a terminal.

**Note:** I initially put some example blackboard bold capitals in this post.
They showed up OK in the editor, but the saved post was truncated right where
I put the capitals. So there must be some bugs in WordPress’ Unicode handling.

**Note 2:** I initially had `Compose-~-~` for a nonbreaking space, but it
turns out `Compose-<space>-<space>` already does that.
