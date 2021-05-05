+++
date = 2019-05-16T08:45:24-06:00
title = "Print to the reMarkable Cloud from a Fedora computer"
weight = 0 # all howtos have zero weight => alphabetical ordering
template = "howto.html"
+++

I recently picked up a [reMarkable] tablet and am really enjoying it! One neat
thing is that it is well-integrated with a backing cloud service, so that with
the right setup you can “print” from a computer straight to the [reMarkable].
Here’s a setup that worked for my Fedora machine. The directions are primarily
derived from the [remarkable-cups] instructions put together by [Mark Meyer].

**Note**: This is post-facto and is probably missing some steps.

1. Install [rmapi]; binaries available [here][rmapi-binaries].
2. Several SELinux-y steps that may be somewhat confused:
   1. Copy/move the binary to `/usr/bin`.
   2. Set its SELinux permissions:  `sudo /sbin/restorecon -v /usr/bin/rmapi`.
   3. Move it to `/var/spool/lpd/rmapi`.
   4. We can probably just leave it in `/usr/local/bin` or something; note however
      that the driver script below hardcodes the executable path.
3. Set up the following script as `/usr/lib/cups/backend/remarkable`, owned by
   root, permissions 755 or so:

   ```sh
   #!/bin/bash
   #
   # Derived from:
   #
   # https://github.com/ofosos/scratch/blob/master/remarkable-cups/remarkable.sh

   backend="$0"
   jobid="$1"
   cupsuser="$2"
   jobtitle="$3"
   jobcopies="$4"
   joboptions="$5"
   jobfile="$6"

   rmapi=/var/spool/lpd/rmapi

   printtime="$(date +"%Y%m%d.%H%M")"
   sanitized_jobtitle="$(echo "$jobtitle" | tr / _)"
   outname=/tmp/"$sanitized_jobtitle - ${printtime}.pdf"

   if [ $# -eq 0 ] ; then
       # this case is for "backend discovery mode"
       echo "Remarkable Printer \"Mark Meyer\" \"Backend to print directly to Remarkable cloud\""
       exit 0
   fi

   if [ -z "$jobfile" ] ; then
       jobfile=-
   fi

   cat "$jobfile" >"$outname"
   "$rmapi" put "$outname" "${DEVICE_URI#remarkable:}"
   rm "$outname"

   echo 1>&2
   exit 0
   ```
4. Follow the instructions on the [remarkable-cups] README to generate a
   `remarkable.ppd` file, and place it in `/etc/cups/ppd`. Permissions should
   be 0o640, owner `root`, and group `lp`.
5. Might need to `restorecon` the PPD and/or backend file as well.
6. Reload or restart CUPS to pick up the new configuration.
7. Add a new printer using your preferred interface. Use a device URI of
   `remarkable:/Printouts`. May need to install `system-config-printer`.
8. Log in to the reMarkable cloud using `rmapi` to generate `~/.rmapi`.
9. Copy `~/.rmapi` to `/var/spool/lpd/.rmapi` and chown to `lp:lp`.
10. Possible `restorecon` that file as well?

[reMarkable]: https://remarkable.com/
[remarkable-cups]: https://github.com/ofosos/scratch/tree/master/remarkable-cups
[rmapi]: https://github.com/juruen/rmapi
[rmapi-binaries]: https://github.com/juruen/rmapi/releases
[Mark Meyer]: https://github.com/ofosos/

To update the `rmapi` binary (if it needs rebuilding or a bugfix), it should
work just to repeat the first few steps above.

**Update 2020-May-29:** It seems that the most recent versions of `rmapi` care
about the extension of the filename that you upload. I’ve modified the above
script to hardcode `.pdf`. Maybe it needs to be smarter?
