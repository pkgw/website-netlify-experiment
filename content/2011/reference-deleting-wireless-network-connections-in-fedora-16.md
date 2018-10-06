+++
date = 2011-12-20T07:33:42Z
title = "Reference: Deleting wireless network connections in Fedora 16"
path = "2011/12/reference-deleting-wireless-network-connections-in-fedora-16"

[extra]
wp_rel_permalink = "/2011/12/reference-deleting-wireless-network-connections-in-fedora-16/"
wp_shortlink = "/?p=490"
+++

It took me a few tries to figure out how to delete a wireless connection from
[NetworkManager](http://projects.gnome.org/NetworkManager/) on
[GNOME](http://gnome.org/) 3.2 systems (such as
[Fedora](http://fedoraproject.org/) 16).

As far as I can tell, there’s no GUI way to do it.

It appears as if you should be able to remove connections with the
command-line interface program `nmcli` with something like `nmcli con delete
id "Auto NetworkName"` but that doesn’t seem to work for me. (Nor does it
result in an error message.)

However, if I go to `/etc/sysconfig/network- scripts` and blow away the files
corresponding the connection that I want to remove (`sudo rm -f
*NetworkName`), the connection appears to get deleted. It’s at least no longer
reported in `nmcli con list`.
