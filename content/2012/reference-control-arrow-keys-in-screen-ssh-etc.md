+++
date = 2012-03-10T10:44:06Z
title = "Reference: Control-arrow keys in screen, SSH, etc."

[extra]
wp_rel_permalink = "/2012/03/reference-control-arrow-keys-in-screen-ssh-etc/"
wp_shortlink = "/?p=518"
+++

I’ve often had trouble with the keybindings Control-Leftarrow and Control-
Rightarrow not doing what I want on “nonstandard” terminals: SSHing into Macs,
some GNU screen instances, etc. I think the basic issue is that there are
several ways to bind these keys, and some systems don’t have systems set up to
cover all of the cases. Here’s the `~/.inputrc` file that does the trick for
me:  "\\e\[5C": forward-word "\\e\[5D": backward-word "\\e\[;5C": forward-word
"\\e\[;5D": backward-word "\\e\[1;5C": forward-word "\\e\[1;5D": backward-word
"\\e\\e\[C": forward-word "\\e\\e\[D": backward-word Meta-.: yank-last-arg
Meta-\_: yank-last-arg  With a bonus explicit binding of Alt-period, which is
also sometimes missing. In my explorations I discovered that for SSHing into
OS X / Darwin computers, the third pair is the one that’s relevant.
