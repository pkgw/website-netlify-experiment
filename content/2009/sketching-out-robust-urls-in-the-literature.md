+++
date = 2009-04-24T21:38:11Z
title = "Sketching Out Robust URLs in the Literature"
path = "2009/04/sketching-out-robust-urls-in-the-literature"

[extra]
wp_rel_permalink = "/2009/04/sketching-out-robust-urls-in-the-literature/"
wp_shortlink = "/?p=115"
+++

For a while now, lots of scientific papers have included links to websites
that provide important non-textual supplements to papers: large tables or
images, software source code, and so on. My impression is that most people are
aware that can be problematic. URLs tend to go stale after only a few years,
and I suspect that this is especially true of the ones published in the
scientific literature, since people spend a lot of time moving from
institution to institution as postdocs. (It would be an interesting exercise
to go through some set of papers on [the arXiv](http://arxiv.org/) and assess
the half-life of a published URL.) But most people (rightly) don’t worry about
these things much and we’re steadily building up a literature that, in many
important aspects, has an expiration date.

It would be nice to do a bit better job of this. This would naturally, I
think, be the responsibility of the journal publishers — they have an interest
in the durability of their product, and they can enforce standards when it
comes to these things. And indeed they seem to have converged on an “online
supplement” / “electronic edition” model where online resources are alluded to
in the published paper but no URL is given. I assume this is to give them the
flexibility to change the URL in the future, which is something I can’t fault
them for wanting to do. Who wants to commit to running a webserver at a
specific domain name hosting specific files in the year 2060?

But the publishers don’t seem to insist that _all_ important material be
hosted by the journal. Source code, in particular, is often hosted at external
sites. This makes sense: source code tends to get updated, and while it’d be
valuable to host a static copy of code as it was used to create a published
work, it’s likely more valuable have a changing website giving the latest
information about and updates to that code. (If I had my druthers I’d also
require that _any_ paper giving the results of running _any_ software _had_ to
publish the source to that software as well, but that’s not happening anytime
soon.) So I can see where the publishers are coming from. They (rightly) don’t
want to get into the business of hosting websites for random scientists’
projects.

So, how could we provide robust links in the literature to evolving content?
We want something that will last even if the person in charge of a project
changes institutions, or if a new person takes over a project, and ideally
something that should last on a 50-year timescale. And it shouldn’t require
scientists to have to know too much about web stuff. (But I don’t think you
can get away with knowing nothing. If you’re publishing something in a paper
you’re making a commitment to it and you should understand what you’re
committing to.)

I think the simplest solution is to take an approach similar to that used by
the [PURL](http://purl.oclc.org/) people. In that system, you register some
kind of permanent URL and tell the registrar the “real” URL of your
information. Requests for the permanent URL are forwarded to the real URL.
And, vitally, if you have to move the “real” URL, you can do so without
breaking the permanent URL.

It seems to me that it would make more sense, however, to do this in DNS,
rather than with HTTP redirects as PURL does. You could have some toplevel
site, let’s call it example.org, and let people register
myscience.example.org. (I came up with an astronomy-centric name for such a
service that I  thought was good but, alas, it was a porn site.) The key here
is that myscience.example.org can be set to resolve to any IP address that you
want, and if you can get a webserver under your control (not too much to ask,
I think), then you can configure it to respond to requests for
myscience.example.org with your particular content. As with PURLs, if you need
to move your hosting, you change the IP address and configure a new webserver.
This difference makes the service much easier to run — all you need to do, at
a minimum, is maintain control of the domain name and update your DNS records
as needed. You don’t have to deal with traffic spikes caused by your
registrants. A completely user-unfriendly implementation wouldn’t even need
its own webserver.

Several elaborations can be envisaged:

- Namespacing probably needs to be dealt with — it’s unfair if I can get my
  hands on stars.example.org and hold onto it forever. There are various ways
  you could deal with this.
- You could associate each subsite with the paper that it was published in and
  the particular URLs that were published. You could then periodically check
  that those URLs were live and nag the registrant if not.
- If registrants worry about being scooped, you could let them assert priority
  in secret. They send you a request with a one-way hashed  version of the
  name of subsite they intend to register. Because of the one-way function,
  the registrar can know if anyone else has requested the same name without
  having to know what the actual name is. Then when your paper is released you
  can reveal your domain name and have documentation of when you first
  (secretly) requested it. Would require social protocols to prevent abuse.
- You could go into web hosting and host the sites for people that didn’t want
  to deal with the server stuff.

You could also go into email hosting. A similar problem to broken URLs is
broken email addresses — papers are published with the authors’ email
addresses, and these often go bad as people move around. You could grant
people someusername@email.example.org and forward it to their current
institutional address. (This looks a little classier than publishing your
gmail.com address in a paper.) And again as they move around, they could
update the address that gets forwarded the mail. Because you have to run a
forwarding mail server, this requires more effort to implement than the DNS
system, but it’s not a big deal.

This latter bit, however, gets into all the usual tricky identity questions.
When do you expire usernames? What do you do if your name changes? How are two
people with the same name distinguished?

This latter issue is an annoying one in science. How do we distinguish papers
published by different J Smiths? (Or P Williamses — not that I’m bitter.) How
can you know that John Smith changed her name to Jane Smith? Is the J Smith at
Institution A the same person as the J Smith at Institution B? Far too much
insider knowledge is required to be able to answer these questions reliably.
These are well-known to be tough issues to deal with. It’d be nice to see more
effort to tackle them in the relatively small and well-behaved scientific
circle, though. The arXiv is
[starting to make an effort](http://arxiv.org/help/author_identifiers), but a
lot more people will need to get involved for it to really take off.

(The arXiv “author identifier” thing is what got me musing about this to begin
with. There are two issues with their work that I’ve noticed so far. Firstly,
of course, this is specific to arXiv. Nowadays most stuff appears on it, but
I’m not sure how well it can scale. Secondly, for a paper to appear as “yours”
in their author identifier list
\[_e.g._ [mine](http://arxiv.org/a/williams_p_1)\], you have to be an “owner”
of that paper, which typically only the first author is. They seem to want all
authors to be listed as owners, and I can see how that is perhaps what makes
the most sense formally, but practically I don’t think it happens much. Maybe
community standards will change in that regard.)

(Also, in the course of reading about that feature, I noticed that the
development and management of the arXiv are totally opaque. I think they’re
motivated by a desire to not spend all their time dealing with crazy people,
but I still find that very disappointing. Crazy people don’t care about the
source code to arXiv, but the source completely closed, there are no ways for
people to join in, and there isn’t even communication about the development
plans! Not cool.)
