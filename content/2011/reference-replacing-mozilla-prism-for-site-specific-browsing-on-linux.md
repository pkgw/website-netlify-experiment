+++
date = 2011-09-27T11:30:53Z
title = "Reference: Replacing Mozilla Prism for Site-Specific Browsing on Linux"
path = "2011/09/reference-replacing-mozilla-prism-for-site-specific-browsing-on-linux"

[extra]
wp_rel_permalink = "/2011/09/reference-replacing-mozilla-prism-for-site-specific-browsing-on-linux/"
wp_shortlink = "/?p=457"
+++

[Mozilla](http://mozilla.org/) briefly offered a little program called
[Prism](http://www.mozillalabs.com/en-US/prism/) that let you build a
[site-specific browser](http://en.wikipedia.org/wiki/Site-specific_browser)
(SSB): a browser with a stripped-down interface that is intended for
interacting with one particular site. The idea is that if you plan to stay
entirely on one site during a browsing session, nowadays you often don’t
really need the location bar, back and forward buttons, history, etc. This may
sound silly, but I’ve found stripped-down SSB interfaces much nicer than those
of regular browsers, when they’re appropriate.

Mozilla says it’s dropped Prism in favor of a project called
[Chromeless](http://www.mozillalabs.com/en-US/chromeless/index.html).
Unfortunately Chromeless seems to have very different goals, and it appears to
have no support at all for saying, “Please make an SSB for this webpage now.”
The development of Chromeless has also been very slow recently. Meanwhile,
Prism isn’t entirely compatible with Firefox 3 and above, which has been bad
news for my SSB-loving self.

I’ve looked into this a bit, and it turns out that
with recent versions of [Firefox](http://www.mozilla.org/firefox/), the
capabilities of the old Prism can be emulated. I’ve done this on Linux, but
similar approaches ought to be workable on other OSes. The limitations that I
know of are:

- It’s a hassle to set up a new SSB.
- External links open in the SSB UI, not your default Firefox UI.
- (This one is **fixed** in Firefox 10! It makes a big difference since you
  don’t have to keep a spare “regular” Firefox window lying around at all
  times.) If you open an SSB UI without a default Firefox UI existing,
  attempts to create new Firefox windows will create windows in your SSB UI.
- If you try to launch an SSB twice, you’ll get a complaint about Firefox
  being running but unresponsive.
- The icons for running applications aren’t differentiated.

That being said, here are the instructions for replacing Mozilla Prism on a
Linux system.

- In a terminal, run `firefox -ProfileManager -no-remote`.

- Create a new profile.

- Give it a name related to the website you want to make an SSB for. Mozilla
  recommends that profile names be all-lowercase and not contain spaces. My
  example will be “gdocs”; for multiple SSBs, just replace “gdocs” with a
  different name in everything that follows.

- Start up the browser using this profile.

- Navigate to the main page for your site.

- In the Preferences screen, set the Home Page to the current page. If the URL
  contains bits that look superfluous, edit them out. (You can test the
  homepage setting by hitting Alt-Home to see if the bits really were
  superfluous.)

- In the Tabs section of the Preferences screen, turn off “Always show the tab
  bar” and “Open new windows in a new tab instead”.

- (Extra credit — these bits will give your SSB launcher the icon of your
  chosen website.) Hit `Control-I` to get the Site Information window. Choose
  the Media section, find the image that corresponds to the website’s bookmark
  icon — this is usually the first image and is usually called favico.ico. Use
  the “Save As…” button to save it somewhere. * In the View → Toolbars
  submenu, disable as many of the toolbars as you want. If you disable the
  menu bar, it can be recovered by hitting `Alt-f`. (This feature is only
  available in newer Firefoxes; it’s definitely present in update 7.)

- (Extra credit part II.) Convert the downloaded site icon to a PNG named
  `~/.local/share/icons/ssb-gdocs.png`. The aptly-named command-line tool
  `convert` is fine for this.

- Create a file called `~/.local/share/applications/ssb-gdocs.desktop.` Fill it
  with contents resembling the following:

  ```
  [Desktop Entry]
  Name=GDocs
  Type=Application
  Comment=Google Documents
  Exec=firefox -P gdocs -no-remote
  Icon=ssb-gdocs.png
  ```

  If you haven’t been doing the extra credit, use
  `Icon=redhat-web-browser.png` on Fedora machines.

- Repeat the above steps for as many SSBs as you’d like to create. When done,
  _exit all Firefox instances_, SSBs and default profile alike. Run `firefox
  -ProfileManager`. Select your default profile, and start up Firefox. This
  step is necessary to tell Firefox that you want it to start up using your
  default profile by default.

- On Fedora systems, a launcher for your SSB will appear in the Other section
  of your Applications menu. You can drag this launcher onto your desktop or
  the panel if you want.
