+++
date = 2011-05-25T00:36:13Z
title = "Reference: What to Do If Fedora 15 Locks Up on Login"
path = "2011/05/what-to-do-if-fedora-15-locks-up-on-login"

[extra]
wp_rel_permalink = "/2011/05/what-to-do-if-fedora-15-locks-up-on-login/"
wp_shortlink = "/?p=407"
+++

I just tried installing the just-released
[Fedora 15](http://fedoraproject.org/), which comes with the new
[GNOME 3](http://gnome.org/) user interface. As expected, the new software has
some rough edges … well, it freezes my computer as soon as I try to log in.
(I’m not angry about this since F15+GNOME3 is bleeding-edge software, with
lots of churn in the graphics code, which tends to be both hard-to-test and
disaster- prone. I did this install on a noncritical machine of mine with the
two-sigma expectation that it wouldn’t work.)

If GNOME 3 thinks your desktop doesn’t support 3D acceleration, it will use a
“fallback mode” that avoids it. This sounded like what I needed, since Linux
lockups on desktops are almost always associated with 3D graphics drivers.
Unfortunately, the only documented way to turn on fallback mode is through the
graphical interface, which I couldn’t get to.

The best method that I could discover to fix this is as follows:

1. Boot up the machine in single-user mode, by pressing keys during bootup,
   then editing the GRUB kernel arguments to add a “1” at the end of the
   kernel command line. (The “1” can be thought of as implying “single-user
   mode”.)

2. Run: `rpm --nodeps -e gnome-shell`

3. Exit the root maintenance-mode shell.

4. Log in as your regular graphical user. You should be brought into fallback
   mode.

5. Force fallback mode permanently via the GUI: user menu → System Settings →
   System Info → Graphics → Force Fallback Mode: on.

Why the `--nodeps`? Because the gnome-panel package, which is needed to use
the fallback mode, requires gnome-shell, the new GNOME 3 UI, “to band aid
upgrades”, according to the RPM changelog.

You might think that there would be a text-mode way to change the setting. And
it seems that there should be. The `org.gnome.desktop.session.session-name`
[GSetting](http://live.gnome.org/GnomeGoals/GSettingsMigration) needs to
changed from “gnome” to “gnome-fallback”. From my read of the docs, it should
be possible to do this by running the command:

```sh
gsettings set org.gnome.desktop.session session-name \'gnome-fallback\'
```

(The escaped single quotes are necessary.) When I tried this from a text
login, it didn’t give any indication of failure, but didn’t do anything.
[This page](https://wiki.archlinux.org/index.php/GNOME) suggests that the
command should be run with the environment variable `GSETTINGS_BACKEND=dconf`,
but that didn’t change anything for me. My extrapolation was that the
following command should also have done the trick:

```sh
dconf write /org/gnome/desktop/session/session-name \'gnome-fallback\'
```

but this gave a [DBus](http://www.freedesktop.org/wiki/Software/dbus) error
involving the inability to connect to an X11 server. It would surprise me if
[DConf](http://live.gnome.org/dconf) required an X11 connection, but perhaps
it does.
