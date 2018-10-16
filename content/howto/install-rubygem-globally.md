+++
date = 2018-08-21T00:00:00-04:00
title = "Install a rubygem Globally"
weight = 0 # all howtos have zero weight => alphabetical ordering
template = "howto.html"
+++

… on Fedora, that is. Example gem name, obviously.

```sh
sudo gem install --no-user-install --minimal-deps \
  -r -i /usr/share/gems winrm-elevated
```

But I am starting to conclude that it’s better to configure your Ruby/Gem
installation to use a personal Gem repository all the time. I think you
do that with something like:

```sh
export GEM_HOME=$HOME/.gem
```

But I don’t feel like I understand Ruby packaging at all so maybe that’s
terrible advice.
