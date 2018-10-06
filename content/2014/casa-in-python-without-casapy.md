+++
date = 2014-02-20T08:42:24Z
title = "CASA in Python without casapy"
path = "2014/02/casa-in-python-without-casapy"

[extra]
wp_rel_permalink = "/2014/02/casa-in-python-without-casapy/"
wp_shortlink = "/?p=836"
+++

**Update (2017 July):** This instructions might still be helpful in some
cases, but I now provide compiled packages of the CASA Python libraries based
on the [conda-forge](https://conda-forge.org/) project, which achieve the same
effect in a _much_ more reliable manner. I haven’t written full instructions
yet but [here’s the landing page](https://anaconda.org/pkgw-forge/casa-python)
for the key package.

Like several large applications, [CASA](http://casa.nrao.edu/) bundles its own
Python interpreter. I can totally understand the decision, but sometimes it’s
really annoying when you want to combine CASA’s Python modules with personal
ones or those from another large package.

Fortunately, it’s not actually that hard to clone the CASA modules so that
they can be accessed by your system’s Python interpreter — with the major
caveat that _the procedure might totally fail if the two different
interpreters aren’t binary-compatible_. I’ve had success in the two attempts
I’ve made so far, though.

Really all you do is copy the key files. There’s a wrinkle, however, in that
you need to set up the dynamically-linked libraries so that they can all find
each other. This can all work automatically with the right
[RPATH/RUNPATH](http://en.wikipedia.org/wiki/Rpath) settings in the binary
files, but empirically _99% of programmers are too clueless to use them
correctly_. Grrr. Fortunately, a tool called
[patchelf](http://nixos.org/patchelf.html) helps us fix things up.

Anyway, here’s how to equip an arbitrary Python interpreter with the key
`casac` module — subject to binary compatibility of the Python module systems.
I’m assuming Linux and 64-bit architecture; changes will be needed for other
kinds of systems.

1. Download and install [patchelf](http://nixos.org/patchelf.html). It’s
   painless.

2. Download and unpack a
   [CASA binary package](http://casa.nrao.edu/casa_obtaining.shtml). We’ll
   call the CASA directory `{CASA}`.

3. Identify a directory that your Python interpreter will search for modules,
   that you can write to. The global directory is something like
   `/usr/lib64/python2.7/site-packages/`, but if you have a directory for
   personal python modules listed in your `$PYTHONPATH` environment variable,
   that’s better. We’ll call this directory `{python}`.

4. Customize the following short script to your settings, and run it:

   ```sh
   #! /bin/sh
   
   casa={CASA} # customize this!
   python={python} # customize this!
   
   cd $casa/lib64
   
   # copy basic Python files
   cp -a python2.7/casac.py python2.7/__casac__ $python
   
   # copy dependent libraries, with moderate sophistication
   for f in lib*.so* ; do
     if [ -h $f ] ; then
       cp -a $f $python/__casac__ # copy symlinks as links
     else
       case $f in
         *_debug.so) ;; # skip -- actually text files
         libgomp.*)
           # somehow patchelf fries this particular file
           cp -a $f $python/__casac__ ;;
         *)
           cp -a $f $python/__casac__
           patchelf --set-rpath '$ORIGIN' $python/__casac__/$f ;;
       esac
     fi
   done
   
   # patch rpaths of Python module binary files
   cd $python/__casac__
   for f in _*.so ; do
     patchelf --set-rpath '$ORIGIN' $f
   done
   ```

5. At this point you can blow away your unpacked CASA tree, though certain
   functionality will require files in its `data/` directory.

All this does is
copy the files (`casac.py`, `__casac__/`, and dependent shared libraries) and
then run `patchelf` on the shared libraries as appropriate. For some reason
`patchelf` fries the `libgomp` library, but that one doesn’t actually need
patching anyway.

After doing this, you should be able to fire up your Python
interpreter and execute

```python
import casac
```

successfully, showing that you’ve got
access to the CASA Python infrastructure. You can then use the standard CASA
“tools” like this (assuming you’re using CASA version > 4.0; things were
different before):

```python
import casac
tb = casac.casac.table()
ms = casac.casac.ms()
ms.open('vis.ms')
print(ms.nrow())
ms.close()
```

I’ve written some modules that provide higher-level access to functionality
relying only on the `casac` module:
[casautil.py](https://github.com/pkgw/pwpy/blob/master/intflib/casautil.py)
for low-level setup (in particular, controlling logging without leaving turds
all over your filesystem), and
[tasklib.py](https://github.com/pkgw/pwpy/blob/master/intflib/tasklib.py) for
a scripting-friendly library of basic CASA tasks, with a small shim called
[casatask](https://github.com/pkgw/pwpy/blob/master/intfbin/casatask) to
provide quick command-line access to them. With these, you can start
processing data using CASA without suffering the huge, irritating overhead of
the `casapy` environment.

**Note:** for Macs, I believe that instead of `patchelf`, the command to run
is something like `install_name_tool -add_rpath @loader_path libfoo.dylib` —
but I haven’t tested this.
