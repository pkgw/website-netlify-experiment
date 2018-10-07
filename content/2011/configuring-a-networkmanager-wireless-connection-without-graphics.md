+++
date = 2011-05-25T00:55:26Z
title = "Reference: Configuring a NetworkManager Wireless Connection without Graphics"
path = "2011/05/configuring-a-networkmanager-wireless-connection-without-graphics"

[extra]
wp_rel_permalink = "/2011/05/configuring-a-networkmanager-wireless-connection-without-graphics/"
wp_shortlink = "/?p=409"
+++

Say, hypothetically, that you
[install a new Linux distribution](http://fedoraproject.org/) and
[your machine locks up whenever you try to log in graphically](./2011/what-to-do-if-fedora-15-locks-up-on-login.md).
You might want to set up a wireless connection to see if there are system
updates available that might fix the problem. If your system uses
[NetworkManager](http://live.gnome.org/NetworkManager/), it might not be clear
how to accomplish this.

The
[NM SystemSettings page](https://wiki.gnome.org/Projects/NetworkManager/SystemSettings)
and
[settings specification document](http://projects.gnome.org/NetworkManager/developers/settings-spec-08.html)
are useful references, but don’t pull the full answer together. You want to
create a file in `/etc/NetworkManager/system-connections/`, named whatever you
like. It should be owner `root:root` and mode 600. The contents should look
like:

```
[connection]
id=Argh
uuid=11111111-1111-1111-1111-111111111111
type=802-11-wireless
timestamp=0

[802-11-wireless]
ssid=SEE BELOW
mode=infrastructure
security=802-11-wireless-security

[802-11-wireless-security]
key-mgmt=wpa-psk
psk=YOUR-NETWORKS-PASSWORD-IN-PLAINTEXT

[ipv4]
method=auto
```

Obviously this only works for WPA/PSK mode, but I think that’s by far the most
common for encrypted WiFi networks these days.

The SSID is specified as a byte
string. If your SSID is expressible in ASCII you can generate this with a
Python snippet like:

```python
';'.join(str(ord(c)) for c in 'SSID')+';'
```

For instance, the network ‘Sample’ is expressed as `83;97;109;112;108;101;`.
No quotation marks are used in the config file.

NetworkManager appears to monitor the `system-connections` directory, and may
initially reject your file if it doesn’t have the restrictive permissions it
wants. Editing the file after the permissions have been changed causes that to
be reloaded. The command `nmcli con up id Argh` should activate the
connection.
