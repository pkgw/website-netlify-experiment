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

1. Install [rmapi]. As of writing, the command is `go get -u
   github.com/juruen/rmapi`.
2. Copy the resulting binary from `~/go/bin/rmapi` to `/var/spool/lpd/rmapi`,
   for reasons that I forget.
3. Set up the following script as `/usr/lib/cups/backend/remarkable`, owned by
   root, no unusual permissions:

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
   outname=/tmp/"$sanitized_jobtitle - $printtime"

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
5. Add a new printer using your preferred interface. Use a device URI of
   `remarkable:/Printouts`.

[reMarkable]: https://remarkable.com/
[remarkable-cups]: https://github.com/ofosos/scratch/tree/master/remarkable-cups
[rmapi]: https://github.com/juruen/rmapi
[Mark Meyer]: https://github.com/ofosos/
