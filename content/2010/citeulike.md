+++
date = 2010-10-03T13:01:59Z
title = "CiteULike"

[extra]
wp_rel_permalink = "/2010/10/citeulike/"
wp_shortlink = "/?p=354"
+++

While getting ready for my qual, I started using the website
[CiteULike](http://citeulike.org/) to keep track of papers to read. It’s one
of many pieces of [reference management
software](http://en.wikipedia.org/wiki/Reference_management_software) out
there that are meant to help scholars keep track of the articles, books,
websites, _etc._ to which they refer in the course of their work.  In my
experience, it’s hugely valuable to think of programs in terms of the data
they generate or modify, and from this perspective all reference management
programs are extraordinarily simple: they maintain 1) a database of
bibliographic information and possibly 2) some of the referenced content
(_i.e._, a bunch of article PDFs). To me, data like these _cry out_ to be
stored in the cloud and accessed through a web app: there are all of the usual
benefits of online storage, and the operations on the data are so
straightforward that it’s really hard to imagine that a client application is
actually necessary with 2010 (or probably even 2005) web browsers.  Based on
my experience with CiteULike so far, web-based reference managers work out
really well in practice. CiteULike provides a Javascript bookmarklet to add
papers to my library, so if I’m reading an article abstract on
[ADS](http://adsabs.harvard.edu/), [ArXiV](http://arxiv.org/), or a journal
website, I can just add it to my library and know I’ll be able to dig the
article up later — since CiteULike is a web app, I don’t have to worry about
which particular computer I’m using or which computer I’ll be in front of when
I need to actually read the article. The kind of flexibility that this gives
you is, I think, really great. And it’s also relieving to know that my
bibliography information is backed up and not just sitting on a single fragile
hard drive. (Well, I don’t actually know that this is the case, but I guess
I’m a trusting sort.)  There are several features that I’d like to see in a
web-based reference management tool that CiteULike doesn’t have, and as far as
I can tell none of its peers do either. The most important is good integration
with bibliography databases like the aforementioned ADS. In the summary page
for every paper I’d really like to see a list of its references with links to
their abstracts. I’d like to be able to run a search like, “Show me papers
that are frequently cited by the papers already in my library.” Other tools
out there seem to have better support for this, though I don’t get the
impression that any of them have integration as tight as I’d like to see.
Another feature I’d like to see is automatic background retrieval and storage
of article PDFs, so I can know that I can always get my hands on the article
itself; this would also allow the reference manager to do full-text searching
of the articles in my library which would be pretty nice. Most reference
managers let you upload PDFs manually, but all of the information needed to
fetch the PDFs directly is available through modern bibliographic metadata.
My interpretation is that most reference manager tools don’t support these
things for the same reason: the bibliography databases and articles are
copyrighted, so your app can’t generally just go ahead and download the
information you’d like. (There are important exceptions: preprints on ArXiV
are freely available, of course, and ADS is a free service, though I think
there are rate limits for clients.) It seems to me that there’s a pretty
obvious solution of having the user enter login credentials for bibliography
and full-text sites if they have them so your app can at least optionally take
advantage of the services, but for some reason few of the desktop apps and
none of the web-based apps support this, as far as I know. (For app authors,
it’d definitely be a hassle to have to integrate with a bunch of uncooperative
services, but it seems like it’d be well worth the effort.)  One thing that
the desktop apps do that the web apps don’t — yet — is have integrated reading
of article PDFs. That kind of functionality is hard to replicate on the web,
but sites like [Google Books](http://books.google.com/) show us that you can
put something together that’s at least competitive with desktop readers. I’d
be interested to see a sincere effort to do really good web-based article-
reading. I think a webapp that did a really good job of integrating article
reading, citation management, and exploration of the bibliographic database
would be really, really compelling.  Even without these wishlist items, I
still find CiteULike to be a great tool — I’d say that reference management is
one of those problem domains which maps really, really well onto the web app
space. I wouldn’t say that it’s clearly superior to any of its peers, but it
certainly does the job well. (One nice thing is that all of these tools
support [BibTeX](http://bibtex.org/) import and export, so you don’t have to
worry about lock-in.) I don’t think the pieces are in place quite yet for
CiteULike or any of its peers to be must-use scholarly tools, but with some
good design and development effort I can totally envision them becoming that
good.
