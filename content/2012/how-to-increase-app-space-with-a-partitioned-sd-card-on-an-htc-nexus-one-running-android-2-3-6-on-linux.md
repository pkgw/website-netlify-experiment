+++
date = 2012-12-29T13:01:24Z
title = "How to Increase App Space with a Partitioned SD Card on an HTC Nexus One Running Android 2.3.6 on Linux"
path = "2012/12/how-to-increase-app-space-with-a-partitioned-sd-card-on-an-htc-nexus-one-running-android-2-3-6-on-linux"

[extra]
wp_rel_permalink = "/2012/12/how-to-increase-app-space-with-a-partitioned-sd-card-on-an-htc-nexus-one-running-android-2-3-6-on-linux/"
wp_shortlink = "/?p=629"
+++

_This recipe written December 2012. Keep in mind that techniques vary a lot
over time. And, yeah, sorry for the SEOriffic title._

I like a lot about the HTC Nexus One phone, but one of its annoying problems
is that it has a tiny amount of storage space for apps.
[Maps](https://play.google.com/store/apps/details?id=com.google.android.apps.maps),
[Twitter](https://play.google.com/store/apps/details?id=com.twitter.android),
[Firefox](https://play.google.com/store/apps/details?id=org.mozilla.firefox),
[Go SMS Pro](https://play.google.com/store/apps/details?id=com.jb.gosms), and
[K-9 Mail](https://play.google.com/store/apps/details?id=com.fsck.k9) are
pretty much must-haves for me, and they alone almost fill up the phone’s
“internal storage” for apps. It’s basically one-in-one-out for installing
apps, and the constant “space is running low” messages are not only annoying
but also indicate that the phone won’t perform certain important functions.

If you Google around, you’ll see various “app2SD” or “apps2SD” apps or scripts
that promise to let you move apps to the SD card, which isn’t huge (4 GB for
me) but is bigger than the 180 MB of the internal storage. There’s built-in
support for this with some apps on Android 2.3.6, and some of the app2sd tools
seem to be remnants from an earlier time. (Others are probably just trying to
cash in on ignorant people.) You also see people talking about reformatting
your SD card to add an ext-format partition to allow app storage there, which
makes sense; the VFAT filesystem used by the SD cards by default doesn’t
support some of the features needed for system files.

It took me a surprisingly long amount of time to find what seems to be the
current best system:
[Super APP2SD](http://forum.xda-developers.com/showthread.php?t=1888986) by
XDA Developers user
[TweakerL](http://forum.xda-developers.com/member.php?u=3024989) with
assistance from several others. The basic approach is straightforward: in the
early stages of system startup, a partition on the SD card is
[bind- mounted](http://docs.1h.com/Bind_mounts) to a few magic app
directories, redirecting their storage from the internal NAND memory to the
SD. And that’s all you need to do!

As usual, the code written by the XDA
people is a little dubious and scary, and the instructions are not great and
also targeted at Windows users. So I’ve adapted their technique and documented
what I did here. That being said, big thanks to TweakerL and friends for
figuring this out and publishing the technique. The caveats:

- You need a
  [rooted phone](https://newton.cx/~peter/2012/03/reference-how-to-root-an-htc-nexus-one-running-android-2-3-6-on-linux/).

- Of course you run the risk of bricking your phone, killing all your apps,
  etc.

- Apps become substantially slower to load and less responsive. The difference
  is noticeable and annoying. I still prefer having the freedom to actually
  install new apps, which I basically didn’t before, but this downside is
  significant.

- The transfer is all-or-nothing, so you can’t keep a few apps on internal
  storage for faster loading.

- The storage space reports on the phone become inaccurate.

- None of your apps are available if your SD card is unavailable.

- I’ve only been using this system for a little while, so there may be other
  issues that I haven’t yet appreciated.

Here’s how it’s done:

1. Do some preparation.

   1. Root your phone, perhaps using
      [my instructions](https://newton.cx/~peter/2012/03/reference-how-to-root-an-htc-nexus-one-running-android-2-3-6-on-linux/).
      This has its own large set of caveats and hassles. For me, at least, the
      lack of app storage is an annoying enough issue that I’m happy that I
      went to the trouble of the rooting.

   2. You’ll need the [Android SDK](http://developer.android.com/sdk/) and the
      `adb` program. You just need the SDK, not the ADT bundle. My
      [post on rooting](/?p=522) has a bit more info on the installation.

   3. You also need to install Busybox on the phone to get a more powerful
      mount program for later. You install
      [the Busybox app](https://play.google.com/store/apps/details?id=stericson.busybox&hl=en),
      then run it to actually install the needed files. It wanted to place all
      sorts of crazy programs (`httpd`??) that I disabled, but they’re
      probably fine. I think the only truly necessary tools may be `mount` and
      `mknod`.

2. Back up everything, especially your apps (duh), their data, and your SD
   card.

3. Add an ext3 partition to your phone’s SD card.

   1. You backed up your SD card, right? Because you’re about to wipe it.

   2. Somewhat surprisingly, you can do this while your phone is running.
      Connect your phone to your computer via USB and turn on USB storage.
      Don’t mount the VFAT partition.

   3. I added partitions using the very nice
      [GNOME Disks](http://en.wikipedia.org/wiki/GNOME_Disks) program. I
      essentially shrank the first partition (by deleting and recreating it),
      changing it from 4 to 3 GB, and then I created a new ext3 partition of 1
      GB. The volume labels aren’t important. The partitions should be
      primary/bootable. _Android 2.3.6 can’t handle ext4_, so use ext3. Make
      sure that the type of the VFAT partition is W95 FAT32; I had to change
      this manually after making the partition. You should be able to mount
      the VFAT and ext3 partitions on your computer after setting them up and
      verify their setup.

   4. Restore your backup of the VFAT files.

   5. If you disconnect the USB, your phone should reload the SD card and not
      notice any problems. If it does, reformat the card (which the phone will
      offer to do), then reconnect to your computer and figure out what you
      did wrong. For me, it was setting the partition type.

4. Get the ext3 partition mounted on your phone.

   1. This part of the process involved some trial-and-error so I’m not sure
      what’s strictly necessary. I’m _pretty sure_ that you need to reboot the
      phone to get the OS to notice the new SD partition.

   2. Turn on USB Debugging on the phone. Connect the USB and open up a shell
      using the Android SDK’s `platform-tools/adb shell` command. Use `su` to
      become root.

   3. Many of the built-in shell utilities are surprisingly braindead, even
      given that we’re running Unix on a tiny piece of plastic and metal. When
      in doubt, prefix commands with `busybox` to use the Busybox versions,
      which are generally smarter.

   4. Run `busybox mount -o rw,remount /` and `busybox mount -o rw,remount
      /system` to be able to monkey with the filesystem.

   5. You _may_ also need to manually create device nodes to be able to mount
      the ext3 partition. The VFAT partition of the SD card is mounted from
      something like `/dev/block/vold/179:1`, but the Busybox mount program
      seems to cut off the filename at the colon. There seems to be an
      equivalent device node called `/dev/block/mmcblk0p1`, so I created
      `/dev/block/mmcblk0p2` using `busybox mknod` and emulating the
      parameters of the VFAT partition.

   6. After the right magic has happened, I created a mount point at
      `/mnt/sd-ext` and was able to mount the partition with `busybox mount -o
      nosuid,nodev,noatime /dev/block/mmcblk0p2 /mnt/sd-ext`.

   7. Also create a mount point at `/mnt/nand-data` for later.

5. Mirror the apps and data from the internal storage to the SD.

   1. The relevant internal directories are `/data/app` and `/data/data`. The
      XDA Developers approach also mirrors `/data/media/Android`, but I can’t
      find anything resembling this directory on my phone, so I suspect that
      it’s only present in newer Android versions.

   2. Create `/mnt/sd-ext/data/app` and `/mnt/sd-ext/data/data` and duplicate
      the contents of `/data/app` and `/data/data` using your favorite
      technique. You may need to use `busybox cp` and not just `cp` to get
      more useful options. Make sure to preserve permissions, ownership, etc.

   3. I touched `/data/data/this_is_old` and
      `/mnt/sd-ext/data/data/this_is_new` as sanity checks for later.

6. Install the code for futzing with the mounts at boot time.

   1. The trick here is to intercept an invocation of
      `/system/bin/debuggerd`, which is apparently called early in the boot process.

   2. Move `/system/bin/debuggerd` to `/system/bin/debuggerd.bin`.

   3. Create `/system/bin/debuggerd.shim` with the following contents:

      ```sh
      #!/system/bin/sh
      /system/xbin/pkgw.earlymounts
      exec /system/bin/debuggerd.bin
      ```

      I did this using `adb push` onto the VFAT SD card then moving the files.
      You can’t push directly into `/system/bin` because of permissions. Give
      the file permissions and ownership mirroring `debuggerd.bin`.

   4. `cd /system/bin ; ln -s debuggerd.shim debuggerd`

   5. Create `/system/xbin/pkgw.earlymounts` with the following contents:

      ```sh
      #!/system/bin/sh
      export PATH=/sbin:/system/sbin:/system/xbin:/system/bin

      nanddata_dev=/dev/block/mtdblock5
      nanddata_mount=/mnt/nand-data
      sdext_dev=/dev/block/mmcblk0p2
      sdext_mount=/mnt/sd-ext

      busybox mount -o remount,rw /
      busybox mkdir -p $sdext_mount $nanddata_mount
      busybox mount $nanddata_dev $nanddata_mount
      busybox mount -o nosuid,nodev,noatime $sdext_dev $sdext_mount

      if test -f $sdext_mount/data/remount_is_safe ; then
        busybox mount -o bind $sdext_mount/data/data /data/data
        busybox mount -o bind $sdext_mount/data/app /data/app
      fi

      busybox mount -o remount,ro /
      ```

      It should be pretty apparent how it all works. It should also be
      apparent that the device paths and mount paths should be checked against
      the output of `mount` to be sure that everything is pointing in the
      right place. Set ownership and permissions on `pkgw.earlymounts` as with
      `debuggerd.shim`. (The `mkdir -p` above might not be needed? I don’t
      know what persists across boots. I also discovered that the Android
      shell doesn’t have `` as an alias for `test` by default.)

7. Reboot the phone to verify that the shim works. If you log in with `adb
   shell`, the `/data` directory should be unchanged, but the `/mnt/sd-ext`
   and `/mnt/nand-data` should be mounted appropriately right from bootup.

8. Activate the bind mounts.

   1. Enable them by touching `/mnt/sd-ext/data/remount_is_safe`.

   2. Reboot the phone.

   3. Along with the new mounts in `/mnt`, you should see that `/data/data`
      and `/data/app` are mounted from `/dev/block/mmcblk0p2` now. Their
      contents should be identical and your phone should work. But /data/data
      should contain a file called `this_is_new`, not `this_is_old`. Your apps
      are now all living on your SD card!

   4. Check out how much storage your phone thinks it has free in the internal
      app storage space. Try installing a new, large app. The amount of free
      space should remain unchanged. (If nothing else has happened. Firefox’s
      hungry cache ate up some of my space and made me think something had
      gone wrong.)

9. Clean up.

   1. Delete files in `/mnt/nand-data/data` and `/mnt/nand-data/app` to free
      up space on the internal storage. Make sure you’re working in the right
      directory! Try deleting something noncritical, then confirming that it
      still runs on the phone. Reboot again if that’ll make you feel better.
      _Don’t_ delete critical-sounding apps and data in case your SD card
      goes missing. After doing this, my internal storage has 74 MB free,
      which should be enough for all sorts of temporary stuff.

   2. In the app manager, move apps back “from” the SD “to” internal storage —
      even though internal storage is now also on the SD. We’re just
      relocating things from the VFAT partition to the ext3 partition. This
      just makes it so you can still use those apps when you’ve got the VFAT
      mounted over USB.

   3. Go to the app store, go to My Apps, slide over to the All listing, and
      install all those old apps that you removed because of space
      restrictions.

   4. As a side benefit, you can now mostly back up your apps and their data
      directly over USB, rather than by having to use a dedicated backup
      program.

Big thanks to TweakerL and the XDA Developers folks for blazing the trail!

_Update:_ Having been using my phone this way for the past few days, I’m still
happy I did this, but I might consider only moving the app data, and not the
apps themselves, to the SD card. There would still be a lot of space left in
the system storage for a reasonable number of apps, and there’s a possibility
it would help with the responsiveness issues I’m seeing.
