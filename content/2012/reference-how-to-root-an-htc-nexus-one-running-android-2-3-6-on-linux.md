+++
date = 2012-03-13T22:20:32Z
title = "Reference: How To Root an HTC Nexus One Running Android 2.3.6 on Linux"

[extra]
wp_rel_permalink = "/2012/03/reference-how-to-root-an-htc-nexus-one-running-android-2-3-6-on-linux/"
wp_shortlink = "/?p=522"
+++

_This recipe written in March 2012. Keep in mind that the techniques vary a
lot over time._

I recently had to get my [Nexus One](http://en.wikipedia.org/wiki/Nexus_One)
phone repaired, which involved discovering 1) that to do so requires getting
the phone’s data wiped and 2) you need a
[rooted](http://en.wikipedia.org/wiki/Rooting_%28Android_OS%29) phone to
actually back up all of your data. It was too late to be able to back up my
data, but as long as my phone came back wiped, I figured I’d make it so I was
able to back things up thoroughly in the future. This is what I learned.

_Rooting your phone is a pain in the ass._ It took me a long time to figure
out this recipe. Instructions online are usually some combination of
confusing, outdated, inaccurate, or inappropriate. Most instructions reference
[XDA Developers Forum](http://forum.xda-developers.com/) threads which are all
of the above except more so, difficult to browse, and often filled with
useless chatter. (I can see why they do the things they do, but there are a
lot of drawbacks too.) Most of the rooting instructions are for Windows or
Macs. The phone rooters using Linux are, in general, clearly not very familiar
with the OS.

_Rooting your phone voids your warranty and wipes your user data._ Of course,
if you still have a Nexus One, your warranty is probably long gone anyway. In
some versions of [Android](http://www.android.com/), there are ways to gain
root without losing your data, but my impression was that these are more
difficult and rely on exploits that have been closed in Android 2.3.6. (By the
way, Android 2.3.6 is in the “Gingerbread” series; as always, Wikipedia has a
good
[table matching Android codenames and versions](http://en.wikipedia.org/wiki/Android_version_history).)

That being said, here’s the recipe:

1. Preparatory work

   1. Turn on data syncing on your phone in Settings → Privacy → “Back up my
      data”. I have no idea how long it takes for these data to get synced, so
      if the setting wasn’t on before, do this well in advance of actually
      rooting your phone.

   2. Install backup software on your phone and use it. These back up various
      pieces of phone data to your SD card, which can then be transferred to
      your computer over USB.
      [MyBackup Pro](http://www.rerware.com/Android-Backup/) (non-free) seems
      to be the consensus choice. The whole point of this exercise is that
      without root you can’t back up _everything_, but you can back up a lot
      of important stuff like SMSes and call logs. MyBackup Pro wants you to
      create some online account but you can skip that part. (The hands-down
      favorite for general backup is
      [Titanium Backup](http://matrixrewriter.com/android/), but it requires
      root access, which we don’t have yet.)

   3. Back up your phone’s SD card onto your computer using the USB cable.
      Free up at least 500 MB on the card to make room for backups. (The
      backup tool won’t run if you have less than this amount free, so it’s
      not like you can get away with less if you don’t have much installed.)
      These backups will include the phone data backups you just made inside
      `rerware/` on the SD card (if you used MyBackup Pro).

   4. Install the [Android SDK](http://developer.android.com/sdk/). Once the
      tarball has been unpacked, you need to run `tools/android` to get a GUI
      that will let you install many of the components actually needed to do
      stuff with the phone. Be sure to install the components for the correct
      version of Android API. Version 2.3.3/API 10 worked for me. You can skip
      all of the vendor-specific packages (some of which take a long time to
      download). In the end, the programs `platform-tools/adb` and
      `platform-tools/fastboot` should be available.

   5. Download a “recovery image,” which is a tool that lets you boot into an
      alternate OS that lets you monkey around with your phone. These all seem
      to be posted on [XDA Developers](http://www.xda-developers.com/). They
      have a
      [Nexus One Recovery Images wiki page](http://forum.xda-developers.com/wiki/HTC_Nexus_One/Recovery_Images)
      that allegedly collects such images. “Amon\_Ra’s Recovery” version 2.2.1
      worked for me: the file’s called `recovery-RA-passion-v2.2.1.img` and I
      got it off
      [this forum thread](http://forum.xda-developers.com/showthread.php?t=611829).
      Just to be clear, many of the following steps assume that you’re running
      this recovery image or a very similar version thereof.

   6. Download a “superuser utility,” which is a combination of Android
      software (“APK”) and some low-level OS hooks that almost all
      applications build on to do rooty things. There seem to be a ton of
      variants. Almost everybody links to the version mentioned on
      [this XDA thread](http://forum.xda-developers.com/showthread.php?t=682828),
      but the version described there is incredibly out of date. If you trace
      the downloads, they lead to
      [this listing](http://goo-inside.me/superuser/) page, which has more
      recent versions. The file called `Superuser-3.0.7-efghi-signed.zip`
      worked for me. (It was at this point that I realized that not only are
      Android OS versions named after desserts, but those names proceed in
      alphabetical order.)

   7. Set up a [udev](http://en.wikipedia.org/wiki/Udev) file allowing the
      `fastboot` program to identify your phone. This seems a little silly but
      does appear to be necessary. I created a file named
      `/etc/udev/rules.d/99-android.rules`containing these lines:

      ```
      SUBSYSTEM=="usb", SYSFS{idVendor}=="0bb4", MODE="0666", OWNER="peter"
      SUBSYSTEM=="usb", SYSFS{idVendor}=="18d1", MODE="0666", OWNER="peter"
      ```

      The OWNER parameter should be substituted with your username. The syntax
      for these rules is apparently deprecated but whatever.

2. Unlocking the bootloader

   1. Ensure that your SD card is backed up and you have 500 MB of free space
      on it. Prepare to lose all of your data.

   2. Power off your phone. Disconnect it from the USB cable if it’s plugged
      in. (I haven’t verified that you _need_ to do this, but other people’s
      instructions seem to suggest this.)

   3. Boot it into the “fastboot” screen by holding down the trackball while
      pressing the power button. You should quickly get a little semi-textual
      menu screen.

   4. Plug your phone into your computer with the USB. In the Android SDK, run
      `platform-tools/fastboot oem unlock`. If this complains about not being
      able to find your phone, your udev rule may not be functional.

   5. A screen will pop up on your phone asking you if you Really Want To Do
      This. You do. Unless you don’t.

   6. Magic will happen and your phone will boot up. You’ll see a little open
      lock icon at the bottom of the splash screen indicating that the
      bootloader is unlocked.

   7. Reenter your Google account information, Wi-Fi connection password, and
      other basic stuff.

3. Booting into the recovery image

   1. Get back to the fastboot menu: power off, disconnect USB, boot with
      trackball held, reconnect USB.

   2. Run `platform-tools/fastboot flash recovery
      /path/to/recovery-RA-passion-v2.2.1.img`. This should succeed without
      errors.

   3. In the fastboot menu, choose Bootloader.

   4. In the bootloader menu, choose Recovery.

   5. You should boot up into the special recovery mode. NB: I originally
      thought that after I flashed in the special recovery image (step 3B) I
      could boot into this special mode whenever I wanted. In my experience,
      it only works if you boot into recovery mode immediately after flashing
      the image. Otherwise I get a hard lock that requires popping out the
      battery to fix.

4. Monkeying around in recovery mode

   1. Choose the “Nandroid backup/restore” menu option. Back up everything
      that seems reasonable. Since the bootloader unlock has just wiped your
      data, this won’t back up anything personal, but it’ll back up your phone
      OS in case you break things later.

   2. Go back to the main menu (volume down key) and turn on “USB-MS”. (The
      USB cable should still be plugged in from the `fastboot flash` steps.)
      This will activate your phone as a USB filesystem.

   3. Copy your nandroid backup off the SD card (`nandroid/` and potentially
      `.android_secure/`).

   4. Copy your superuser utility _onto_ the SD card.

   5. Unmount the phone on your computer and turn off USB-MS on your phone.

   6. In the main recovery menu, choose “Flash zip from sdcard”, and choose
      your superuser utility. It should print out some messages about what
      it’s doing. You’re now rooted.

   7. In the main menu, reboot into the regular OS.

5. Demonstration of rootiness

   1. Besides back up your data, one thing you can do while rooted is remove
      built-in applications. To get started, turn on “USB Debugging” in the
      Settings → Applications → Development menu on your phone, and plug in
      the USB cable.

   2. In the Android SDK, run `platform-tools/adb shell`.

   3. This is a tiny little [busybox](http://busybox.net/) shell running on
      your phone. You can `ls` and see the contents of your phone’s builtin
      storage.

   4. And you should be able to run `su` to get root access. Do so.

   5. Remount the /system partition in read-write mode: `mount -o remount,rw
      /dev/block/mtdblock3 /system`.

   6. `cd /system/app`

   7. Running `pm list packages -f` will give you a list of installed packages
      and their corresponding APK files, which are found in this directory. To
      remove a package, first manually delete its APK file, then run `pm
      uninstall [ident]`, where `[ident]` is the Java-style name of the
      package such as `com.facebook.katana`.

   8. Close shell, disconnect USB, disable USB debugging, etc.

6. Cleanup

   1. Your phone should now be booted into your regular, barely-initialized
      Android OS. Reinstall your backup program and restore backed-up data. If
      using MyBackup Pro, I found that I should _not_ restore my calendar —
      all of my calendar events got duplicated. I also got messages about
      massive deletion of my contacts, and I’m pretty sure I should have
      chosen not to restore those either. At some point all of my Twitter
      “contacts” also got merged into my Google contact list, which was really
      annoying.

   2. Begin the painstaking process of re-inputting all of your settings.
      There are a lot more than you thought.

   3. Remove the udev rules file you created.

   4. If you so desire, clean up some of the backups and things off your SD
      card.

   5. Finally — the main point of all of this — after you’ve had a while to
      get all of your settings back, run a root-powered full backup of your
      phone data, and copy that backup off the SD card. Once you have root,
      consensus seems to be that
      [Titanium Backup](http://matrixrewriter.com/android/) is the gold
      standard.

Here are some of the resources I used when piecing together all of this
information:

- [XDA Developers HTC Nexus One Guides & Tutorials](http://forum.xda-developers.com/wiki/HTC_Nexus_One/Guides_%26_Tutorials)
  and links therein

- [XDA Developers RA-passion-v2.2.1 forum thread](http://forum.xda-developers.com/showthread.php?t=611829)

- [XDA Developers Superuser 2.3.6.1 forum thread](http://forum.xda-developers.com/showthread.php?t=682828)

- [XDA Developers HOWTO Root Nexus One 2.2.1 FRG83D without OEM unlock](http://forum.xda-developers.com/showthread.php?t=959672)

- [XDA Developers Remove built-in apps from ROM](http://forum.xda-developers.com/showthread.php?t=617026)
