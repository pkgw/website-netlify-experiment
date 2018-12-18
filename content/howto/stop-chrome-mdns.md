+++
date = 2018-12-18T16:12:59-05:00
title = "Stop Google Chrome from Using So Much Bandwidth at the CfA"
weight = 0 # all howtos have zero weight => alphabetical ordering
template = "howto.html"
+++

I recently discovered that whenever I start Google Chrome at work, my
computer’s bandwidth consumption goes to ~450 KiB/s and just sits there
indefinitely. No matter what website I visit or anything.

Background downloads? Infinite loop?

No. [mDNS](https://en.wikipedia.org/wiki/Multicast_DNS). The CfA networks
apparently transmit mDNS traffic between just about everybody, and it seems
that there are so many mDNS-enabled machines that the traffic ends up being
completely continuous.

[This StackExchange answer](https://unix.stackexchange.com/a/458656/327504)
ended up doing the trick for me. Apparently there are no user-facing, or even
hidden, preferences to control the Chrome device discovery code that causes all
of the traffic. You have create a “policy file” to alter the behavior:

```sh
echo '{ "EnableMediaRouter": false }' |sudo tee /etc/opt/chrome/policies/managed/no-mdns.json
```

It doesn’t happen on macOS because there Chrome hooks into the system mDNS
implementation, which seems to be smarter about not polling everything all of
the time.
