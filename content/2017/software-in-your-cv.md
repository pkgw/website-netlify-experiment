+++
date = 2017-08-22T15:29:19Z
title = "Software in your CV"
path = "2017/08/software-in-your-cv"

[extra]
wp_rel_permalink = "/2017/08/software-in-your-cv/"
wp_shortlink = "/?p=1056"
+++

As a scientist, I’ve spent a lot of time writing code over the years. Like, [a
lot](https://github.com/pkgw?tab=repositories). You can definitely be a
successful scientist without doing this much coding, but it’s something that
helps me get research done, that I’m really good at, and that I enjoy. I do a
pretty bad job of promoting my software in the community, but it’s important
to me that others can reuse the work that I’ve done and have a better shot of
reproducing my research results.

Because of all this, I’ve spent some time thinking about how to report my
software work on my curriculum vitæ. I’ve seen plenty of CV’s where the author
basically doesn’t mention their software work at all, or condenses it into
single a bullet point line, but I don’t agree with that approach for two big
reasons:

1. Software can be both a substantial time investment and a substantial
  contribution to the field. If you’re proud of it, you should show it off!

2. But even if, hypothetically, you weren’t proud of your work … you may have
   heard that _curriculum vitæ_ translates to “the course of \[one’s\] life.”
   I am a big believer that your (long-form) CV should be an _exhaustive_
   compilation of your professional work. For instance, I think it would be
   unethical to leave a paper off your CV because it turned out to be wrong or
   misguided. If you’ve spent substantial time on a professional undertaking,
   you have a duty to find a way to put it on your CV.

It’s true that it’s not very normal to spend much CV space on software work.
But that norm is a social construct! We can change it. In fact we _should_ do
so if it’s counterproductive — and I think it’s fair to say that there is a
broad the consensus is that we don’t value software contributions enough in
science. Spending more CV space on software work won’t exactly change that
overnight, but it’s a piece of the puzzle.

I suspect that one reason that people don’t put software on their CVs is that
it’s not very clear how to report it. This contrasts with the case of
publications, where the norms are so ingrained that it can be hard to notice
that they even exist. For instance:

- It feels “obvious” that the natural way to measure publications is in units
  of journal articles. Articles count, blog posts don’t. But this is just a
  convention, and not necessarily a well-motivated one: journal articles are
  nice, convenient quanta to work with, but of course it’s possible to
  communicate research in other ways. For instance,
  [Eric Mamajek](http://www.pas.rochester.edu/~emamajek/) posts all sorts
  useful information on sites like
  [Figshare](https://figshare.com/authors/Eric_Mamajek/414430) and Facebook.
  The
  [blog of the well-known film scholar David Bordwell](http://www.davidbordwell.net/blog/)
  is an astounding fountain of professional-grade insight.

- Likewise it feels obvious to quantify the impact of an article through its
  citations, _even though we all know citation counts are a hugely flawed
  metric_. Some people live and die by the _h_\-index; others do an admirable
  job of resisting the temptation to reduce “impact” to this convenient scalar
  number. But we all know that if someone is judging our research output, it
  is likely that they’ll look at citation counts.

So: what’s a Right and Proper way to report software work on a CV?
Here’s what I’ve come up with and tried to implement on [my own CV](./cv.md).

What is the fundamental unit of reporting? I’d say that it used to be a bit
less clear what the answer to this question was, but in the year 2017 the
fundamental unit is now, clearly, the version control
[repository](https://www.sbf5.com/~cduan/technical/git/git-1.shtml). There is
_not_ necessarily a 1:1 correspondence between “software repositories” and
“software projects”, where the latter is some nebulous internal idea that we
have when we think of some particular piece of software. But that’s exactly
the point: a repository is a concrete, tangible thing that you can point
someone to. (Specifically: it’s a set of files plus their modification
history; probably managed by [Git](https://git-scm.com/), but the particular
tool used doesn’t matter.) If I say that I worked on the monitor and control
system for the [HERA](http://reionization.org/) telescope, you can get a
general idea of what I might have done — but if I further specify that this
system is incarnated in the
[HERA-Team/hera\_mc](https://github.com/HERA-Team/hera_mc) repository on
GitHub, you can now discover the _exact_, tangible manifestation of that work.

Like journal articles, pieces of software often have multiple authors.
Sometimes, one has made just a small contribution to a large effort; sometimes
one is solely responsible for the whole thing. It seems important to convey
that to readers of the CV, although maybe someone working in
[a field in which alphabetical author lists are standard](https://en.wikipedia.org/wiki/Academic_authorship#Order_of_authors_in_a_list)
might disagree. (As a person with an alphabetically-late surname, though,
[I definitely prefer our way](http://www.overcomingbias.com/2008/01/the-ordering-of-authors%E2%80%99-names-in-academic-publications.html)!)
Unlike traditional journal articles, however, software packages evolve over
time, and new contributors come and go — something that contributors to
more-modern scientific software papers
[have tried to grapple with](https://github.com/astropy/astropy-v0.2-paper#rules-for-authorship).
How does one convey one’s role in a software package given all this?

For my CV, I’ve chosen to report the total number of commits in each
repository, and the percentage of commits that are mine. I definitely view
this as a “least-bad” approach. Counting commits is problematic, but it’s
probably less bad than counting lines of code, and it’s a metric that’s
guaranteed to be available for every repository that one contributes to. An
author list with a mutually- agreed-upon ordering is not. Listing just the
fraction of commits does elide information about who one’s collaborators are,
which might be of interest, but listing all of the authors adds a lot of noise
for what in my opinion is a very ambiguous gain.

To give a sense of the freshness of my involvement in a project, I put the
list in reverse chronological order of my most recent commit in each repo.
This feels like a pretty reasonable approach to me, although you could imagine
the total timespan of contributions being of interest too.

There’s one last dicey question to consider: conveying impact. While I believe
that a CV should be exhaustive, we have to be realistic: people are using your
CV to evaluate you, and they’re not going to read every single line with
loving care. It would be straight-out foolhardy not to give your readers some
clues as to which entries are worth giving special attention.

There are several ways you can do this. It’s not uncommon to have a list of
“Selected Talks” or “Selected Publications” up front with the remainder placed
farther back. Some people will include citation counts in their publication
list. I do this: my feeling is that at least _some_ readers are going to want
that information, so you might as well just provide it. You could easily
imagine having a “Selected Software Projects” category, but for the past
couple of years I’ve leaned against this approach. I don’t like breaking the
information about one’s talks (or papers or software projects) into two lists
that are far apart from one another, and like all binary classifications,
there are sometimes borderline entries that you’d _kind of_ like to highlight
but definitely aren’t the top priority, and “de-selecting” them probably
causes reader to gloss over them.

It feels kind of gross to advertise impact metrics like citation counts, but
here too I feel like that’s the less-bad approach. For software repositories
on GitHub, there are a couple of easy metrics to report: “stars” and “forks,”
for instance. I’m not a huge fan of the (weak) vendor lock-in that this
approach encourages, but it is a fact that essentially all of my software
projects are in fact hosted on GitHub. So, for now, I report those numbers,
thinking of them as an analog of the citation counts that I provide with my
publications. When someone sees that
[Tectonic](https://tectonic-typesetting.github.io/) has 1000 stars
(`</humblebrag>`), they know that it’s something that’s captured a lot of
attention.

Me being me, I’ve automated the gathering of all this information and the way
it gets rendered into my CV. The process turns out to be quite a hassle! You
can collect some of the necessary stats through GitHub’s API, but some things
need to be determined by searches of GitHub’s activity history data, which are
[made available separately through Google’s BigQuery service](https://cloud.google.com/bigquery/public-data/github).
You have to set up multiple API tokens and such to get it all to work. The
main pieces of the stats-gathering code are
[here](https://github.com/pkgw/worklog-tools/blob/master/wlgithub.py) and
[here](https://github.com/pkgw/worklog-tools/blob/master/wltool#L327).

I’m not completely happy with [the final outcome](./cv.md) by any means. I’ve
never seen another CV with a software section like this, and it feels awkward
to report lame-sounding impact statistics like “stars”. But you can bet that I
want to do justice to this part of my professional life, and this is the best
way I’ve managed to come up with. I wish I had some demonstration that adding
this section does cause my CV to stand out more in people’s eyes; to be
honest, I wouldn’t be surprised if it more often has the opposite effect,
since it draws attention to a line of work that I believe remains strongly
undervalued on average. (“Why are you spending time on all of this programming
stuff when you could be doing science?”) But: “Be the change you want to see
in the world,” right? [Let’s give it a shot](./cv.md#software).
