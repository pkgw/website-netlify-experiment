+++
date = 2013-02-07T15:14:53Z
title = "Reference: Running Chandra cscview on Fedora Linux"
path = "2013/02/reference-running-chandra-cscview-on-fedora-linux"

[extra]
wp_rel_permalink = "/2013/02/reference-running-chandra-cscview-on-fedora-linux/"
wp_shortlink = "/?p=644"
+++

You’re supposed to access the [Chandra Source
Catalog](http://cxc.harvard.edu/csc/) with a Java applet, but it appears
there’s no version of Java compatible with both the applet and Firefox. (In
the sense that many Java versions have big security bugs and Firefox blocks
them.) Thus although there are [recommendations for using the applet on Fedora
Linux](http://cxc.harvard.edu/csc/soft_req.html#linux) I believe they are now
inoperative. Here’s a solution.

1. Download and install the latest Java 1.6 JDK. The JRE won’t cut it since we
   need the `appletviewer` program. The instructions above call for 32-bit,
   but I think that’s only for Firefox compat; 64-bit should be OK.

2. Download a local copy of
   [the HTML for the viewer applet](http://cda.cfa.harvard.edu/cscview/cscview).
   The official version specifies `width="100%"` which `appletviewer` can’t
   handle; I can’t think of a clever way to get around this.

3. Edit the local copy to say something like `width="640" height="480"`.

4. But now we’ve lost the base URL, so create a subdirectory called `client`
   and download the jar files mentioned in the HTML, e.g.,
   [jsamp 1.0.0.0](http://cda.cfa.harvard.edu/cscview/client/jsamp-1_0_0_0.jar).

5. Edit `jdk*/jre/lib/security/java.policy` and copy the
   `java.security.AllPermission` to apply to all applets. Yeah, we’re classy.

6. Finally, run `jdk*/bin/appletviewer file:///path/to/your/cscview.html`.

7. (Optional) Discover the `cscview` doesn’t do what you want. ☹
