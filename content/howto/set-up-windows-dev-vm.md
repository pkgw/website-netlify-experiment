+++
date = 2020-04-13T00:00:00-04:00
title = "Set Up a Windows Development VM"
weight = 0
template = "howto.html"
+++

Steps for setting up a Windows development VM the way PKGW likes. We’re
running it on Linux and VirtualBox.


# Installation

About 80 GiB of free disk space is needed for installation and setup. Fun
times. One the machine is going, only about half of that is needed.
   
1. The key is that nowadays Microsoft makes Windows VM images available freely
   from
   [this website](https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/).
   Download the VirtualBox appliance package.
1. Unzip the Zip file. Delete the Zip file.
1. Open VirtualBox and do “Import Appliance”. I bump up the memory to 8192 and the
   number of processors to 2.
1. Delete the `.ova` file. Its contents will have been unpacked into separate
   VirtualBox files stored in VBox’s default location (for me: `/a/vms/vbox`).
1. Boot up your shiny new VM. The default screen is not very helpful, but if
   you press the `Esc` key, you should get a prompt to log in as the user
   `IEUser`. The universal password is `Passw0rd!`.


# Set up the software environment

This is the most annoying part.

1. In the “Type here to search” box, type in “update”, and click the “Check
   for updates” choice when it eventually appears. Let Windows install its OS
   updates, and reboot if/when needed. Check for more updates — some can only
   be installed after earlier updates have been applied. Repeat until the VM is
   fully up-to-date.
1. Set timezone (right-click taskbar clock).
1. In the “Power & Sleep” section of the Windows settings tool, set the screen
   to never turn off, either on battery or when plugged in. (In the VM, it
   seems that sometimes it's not possible to awaken the screen again if it
   turns off this way.)
1. Install Firefox: <https://getfirefox.com>.
1. Install LastPass: <https://lastpass.com/misc_download2.php>
1. Install Notepad++, <https://notepad-plus-plus.org/>. Note that
   [Atom](https://atom.io/) is a large install and can seriously hamper your
   ability to fit everything you need in the 40 GiB drive allocated to the VM.
1. Install Git Bash.
   1. Download and install it from <https://git-scm.com/download/win> — note
      that it is just referred to as “Git”, not “Git Bash”.
   2. Default options are generally OK, but you’ll probably want to select
      Notepad++ as your text editor.
   3. Start Git Bash via the “Type here to search” box.
   4. Right-click the icon of the running program and choose to pin it to your
      taskbar.
   5. In the bash window, run:
      ```
      git config --global user.name "Your Name"
      git config --global user.email your@email
      git config --global alias.ba "branch -a"
      git config --global alias.ci commit
      git config --global alias.s status
      ```
1. Install miniconda: <https://repo.anaconda.com/miniconda/>. (Miniforge doesn’t
   have Windows yet.)
   1. Download and start installer
   2. Choose to "Add Miniconda3 to my $PATH" despite the discouragement.
   3. With the above, should be able to use `conda` within Git Bash.
   4. `conda config --add channels conda-forge`
   5. `conda update --all`
   6. If planning to do conda conbuilds, install `conda-build`
1. Now, the big one: Visual Studio.
   1. Search for “visual studio install older version” and find the result
      that seems most on-point.
   2. Select to download Visual Studio 2017. You’ll need to sign in to a
      Microsoft account to do so.
   3. Find, download, and launch “Visual Studio Community 2017 (version 15.9)”.
   4. Install just the "Desktop Development with C++" workload.
   6. Start the install. It will take a long time.
   7. When the install is complete, reboot the VM. Sometimes this is necessary
      to apply updates pulled in by Visual Studio; failing to reboot can break
      the VM’s dev tools stack!
   8. Check for updates again and install/reboot as needed.
   9. Start Visual Studio; skip signing into Microsoft account.
   10. Pin it to your taskbar.
   11. Go to Tools → Extensions and Updates and start installing the available
       Visual Studio updates. These may be large downloads that require that
       you exit Visual Studio.
1. Other setup you may wish to perform:
   - Install personal SSH keys ­ you will need some way to transfer files
     between your host machine and the VM. On my machine, the IP address of
     the host machine *as seen from the VM* is `10.0.2.2`, and I can `scp`
     between the two once I start up the SSH server on the host machine.
