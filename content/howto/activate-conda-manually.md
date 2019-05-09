+++
date = 2019-05-09T12:22:10-04:00
title = "Activate a Conda Install Manually"
weight = 0 # all howtos have zero weight => alphabetical ordering
template = "howto.html"
+++

I create a lot of independent
[Miniconda](https://repo.continuum.io/miniconda/) installs that I want to
activate manually. Back in the day, you could just do this by putting
`$PREFIX/bin` in `$PATH`, but things are different now. Namely:

```sh
eval "$(@PREFIX@/bin/conda shell.bash hook)"
```

with the **super important note** that the double quotes are essential!

For reference, here’s the shell script snippet that Conda wants to put in your
`.bashrc`, as of Miniconda 4.6.14, with `@PREFIX@` substituted as appropriate:

```sh
__conda_setup="$('@PREFIX@/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "@PREFIX@/etc/profile.d/conda.sh" ]; then
        . "@PREFIX@/etc/profile.d/conda.sh"
    else
        export PATH="@PREFIX@/bin:$PATH"
    fi
fi
unset __conda_setup
```

(Apparently this comes from `conda init` somehow.)
