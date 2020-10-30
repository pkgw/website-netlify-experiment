+++
date = 2020-12-03T22:36:26-04:00
title = "Get Outta My Repo"
+++

[Daniel Katz][katz] recently wrote [a piece entitled “Software and Software
Metadata”][katz-ssmd] summarizing some of his current thoughts about the
software metadata and what it would take to achieve a sort of [“FAIR-ness” for
software][fair4rs]. As I read the article, I realized that — while I’m 100% on
board with the goals — I’ve actually convinced myself that the implementation
strategy we need is pretty different from what Katz outlines.

[katz]: https://danielskatz.org/
[katz-ssmd]: https://danielskatzblog.wordpress.com/2020/09/29/software-and-software-metadata/
[fair4rs]: https://www.rd-alliance.org/groups/fair-4-research-software-fair4rs-wg

<!-- more -->

I’ve got some bigger thoughts on this topic, but here I just want to focus on
the idea of having software authors provide citation metadata by putting special
files, like [CITATION.cff][cff] or [codemeta.json][cmj], in their source
repositories. This idea is super natural and super appealing, but I think it’s
not the right way to go.

[cff]: https://citation-file-format.github.io/
[cmj]: https://codemeta.github.io/

Here are some questions that illustrate my reasoning:

*What do you do about [monorepos]?* Sometimes repositories contain more than one
project, and it is entirely reasonable for some of those projects to want to be
independently citeable. You could certainly sprinkle multiple `CITATION.cff`
files around the repo, of course. But if you break the assumption of a 1:1
mapping between repos and citeable projects, many seemingly straightforward
architectural decisions become much more complicated ([as my recent experience
can attest][cranko]).

[monorepos]: https://en.wikipedia.org/wiki/Monorepo
[cranko]: @/2020/implementing-software-versioning.md

*What do you do about the time axis?* Say that I create a `CITATION.cff` file
and, as a good citizen, update it with every new release of my software. If
someone is using an older version of my software and gets the citation data from
my repo, they’ll get the wrong information. But if I tell them to get citation
data from a file bundled with the software they’re using, how do I fix mistakes?
How long do I maintain citation instructions for old releases? How do I embed
the DOI of a release into its code if I can only obtain the DOI after making the
release? One can devise answers to these questions, but I think they point at a
more fundamental issue that I’ll draw out below.

*What do you do about closed-source software?* Now, I bow to no one in terms of
eagerness to promote open scientific software. But closed-source tools are out
there, and a good metadata architecture should handle them. In particular, while
I’m more than happy for a system to favor open codes, it’s a very worrisome
“[smell]” to me if open- and closed-source software have to be handled very
differently.

[smell]: https://en.wikipedia.org/wiki/Code_smell

Extending this point, consider the metadata ecosystem for journal articles. Do
we ask authors to include metadata in their “source code”? Absolutely not. In
fact, the metadata that are most important for citeability (e.g., DOIs,
year/volume/page numbers) are not even allowed into the author’s hands — they’re
created *by publishers*, during the publication process, not the writing/coding
process. I think this comparison point is really worth paying attention to — the
empirically successful article citation system emphatically *rejects* the
paradigm that we’re talking about for software!

The example of article citation helps draw out the flaws in the “metadata in
repo” paradigm. We should be citing *published objects*. When we talk about
software, the published object is not the source repository — it’s the
*release*. Citation metadata are data *about* releases, which are *derived from
snapshots of* code repositories. Trying to keep citation metadata *in* the
source repository introduces fundamental, unavoidable sequencing and
synchronization problems: it creates a circularity where there should be none.
You can come up with tactics to deal with the specific issues raised above, but
they’re all symptoms of this fundamental issue.

The specific case of citation metadata isn’t the only one where you run into
problems storing data *about* releases in their source repositories. I’ve
convinced myself that even the everyday task of [assigning version
numbers][cranko] suffers from the same flaws. With my [Cranko][cranko-web]
project I’ve built a tool that aims to address versioning in a way that avoids
these issues, and now that I’ve been using it regularly I’m completely convinced
that this insight is deeply important. Whenever I try to talk to people about
it, I can tell that I haven’t found the words to convey just *why* I feel that
way, but Cranko has truly changed my (software) life.

[cranko-web]: https://pkgw.github.io/cranko/

If this profound flaw is lurking out there, why are we trying to put software
metadata in source repositories anyway? Software and articles are different in
important ways — but what’s the specific issue at play here? I believe that it’s
a factor that’s not often mentioned.

It’s not that software gets updated (we have [living articles] now) and it’s not
that software has source code (TeX in Git works quite nicely, thank you very
much). It’s that *software is self-published*. With a few high-volume
publishers, gathering metadata is easy; with thousands of small publishers, it’s
not. Try another thought experiment: if somehow every software release had to go
through the US Library of Congress, would we be talking about citation metadata
files in repositories? Would software citation even be considered a problem to
be solved? I think not.

[living articles]: https://iopscience.iop.org/article/10.3847/1538-4357/aae58a

While metadata-in-the-repo attempts to solve the problem of distributed metadata
gathering, I believe that the circularity that it introduces means that it is
ultimately a flawed foundation that can’t be safely built upon. And this
perspective motivates a rethinking of what we need to do to fix software
citation — but that will have to wait for a later post.
