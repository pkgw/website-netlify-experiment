+++
date = 2020-07-03T16:13:46-04:00
title = "Implementing Software Versioning"
+++

I’ve recently been working on the [AAS WorldWide Telescope][wwt] web software
stack, and I ended up becoming convinced that I needed to adopt a [monorepo]
model for the bulk of the stack (currently housed in the [wwt-webgl-engine]
repo). I’ve historically been reluctant to go the monorepo route, and one of
the big reasons was that it seemed like tracking versions and making releases
would become huge pains.

[wwt]: https://www.worldwidetelescope.org/home/
[monorepo]: https://en.wikipedia.org/wiki/Monorepo
[wwt-webgl-engine]: https://github.com/WorldWideTelescope/wwt-webgl-engine/

Spoiler alert: they do! On the other hand, even for my non-monorepo projects,
I’ve long been dissatisfied with how I implement the process of establishing
versions and making releases. During my [wwt-webgl-engine] work I spent some
time thinking about why that is, and I’ve devised a new (I think?) approach to
address many of the things that have always bothered me. It’s still not fully
baked, but I think the core idea is promising and worth investigating further.
Here we go …

<!-- more -->

There’s a [TL;DR] that attempts to distill the core ideas if this is too many
words for you.

[TL;DR]: #the-pkgw-versioning-workflow-tl-dr

# Some Boundary Conditions

There are some aspects of my versioning workflow that I’ve found
dissatisfying, but there are other aspects that feel profoundly intellectually
Right and valuable. My thought process has been guided by trying to fix the
parts that I didn’t like while preserving ones that I do. Namely:

- **The Fundamental Axioms of Versioning.** I don’t know what to call this
  concept, exactly, but I have seen cases where people did *not* share it, so
  it’s worth making explicit. When you make a release of a piece of software,
  it should be assigned a version, there should be a specific set of
  associated artifacts, and those artifacts should be immutable. I write
  “software” to keep things concise, but I really mean anything to which these
  concepts sensibly apply — a “versionable” thing.
- **[Git][git] is good.** I believe that Git has taken over the
  version-control world for some very good reasons. I’m perfectly happy to
  assume that all versionable things have their source files (code or
  equivalent) tracked in a Git repository. Even if the backing tool eventually
  changes, I’m quite confident that the underlying model will continue to
  involve a [DAG] of commits with branches and tags.
- **[Semver][semver] is often what you want.** The [semantic versioning][semver]
  standard is powerful and useful. It is also true that there are versionable
  things out there for which semver isn’t a super appropriate choice. Semver is
  fundamentally about things that provide *interfaces*, and some versionable
  things don’t really have interfaces, or have interfaces that essentially never
  change — for instance, some kinds of data sets. But for things that *do*
  interface with each other, the semver approach really does provide a
  tractable, *automatable* mechanism for declaring compatibility between
  hundreds of interacting components.
- **Continuous integration and deployment are great.** They just are! One of my
  favorite recent developments in the software world is that there is a now huge
  ecosystem of free CI/CD tools and services. Indeed, the new versioning
  workflow that I’m envisioning is only possible thanks to these services. I’m
  pretty sure that it took me so long to devise it precisely because I haven’t
  fully internalized the kinds of innovations that this ecosystem makes
  possible.
- **Explicit releases are still necessary.** While I’m a big fan of CD, I
  still believe in the importance of what I’ll call “primary releases” —
  releases where a human has sat down and explicitly decided that this
  particular set of artifacts is “ready” in some sense. (Along with primary
  releases, we might have “pre-releases”, “CD releases”, “automated releases”,
  etc.)
- **[Monorepos][monorepo] happen.** My instincts tell me that monorepos are
  bad, somehow. But as I wrote above, I’ve found myself creating them
  nonetheless. Too bad for my instincts.

[git]: https://git-scm.com/
[DAG]: https://en.wikipedia.org/wiki/Directed_acyclic_graph
[semver]: https://semver.org/


# Problem 1: What Happens Between Releases

Why have I been dissatisfied with my current versioning and release
practices?

I’ll start with an example. Imagine that I have a Python package `mypackage`
whose version is written in its `setup.py` file. When I release version 0.1.0,
I update the version string in that file. I then do a bunch of work and make a
bunch of commits. Eventually I decide to release version 1.0.0, so I bump the
version number in that file and keep on going. This is a bog-standard
workflow. Probably thousands of Python packages are managed this way.

What I don’t like about this scheme is that if someone checks out my
repository at a commit between the 0.1.0 and 1.0.0 releases and installs it,
the installed artifacts will be labeled as 0.1.0 even though they do not
correspond to the official 0.1.0 release. This *really* bugs me at a profound
level. Now, have I ever run into actual support issues due to this kind of
problem? To be honest, I think not! But I’m bothered intellectually, not
pragmatically. If I've got a repository from which I've published version X of
some package, I really want it so that there is at most one commit in that
repository labeled with version X.

“That’s why we have Git tags,” you say. And this is a very good point! It took
me a while to perceive the actual problem in practice. (Assuming that you agree
with me that this all is a problem to begin with.)

The problem is that virtually every software packaging system demands that you
embed version numbers in their metadata files (`setup.py`, `Cargo.toml`,
`package.json`), and those files are tracked in Git. As long as those version
numbers are stored in various files scattered around the repository, there is
ambiguity, because the existence of these files essentially forces you to
assign version numbers to commits even when they don't correspond to primary
releases.

Put another way, release tags answer the question of “Which exact Git commit
corresponds to this release?”, but doesn’t offer a coherent model for thinking
about the reverse question: what version number do we assign to the *commits*
between releases? And as long as you have files like `package.json` in your
repo, you have to offer some kind of answer to this question. This is even
more true if you’ve got a continuous deployment pipeline that is creating
artifacts from commits in your repo that don’t correspond to primary releases.


# Problem 1a: Semver and Prereleases

This raises an obvious topic: prereleases. Back in the day, after I released
version 0.1.0 of a package, I might immediately bump its version to 0.1.0.99.
Nowadays, with [semver], I might update to version `0.1.0-dev.0`. To backtrack
on what I just wrote, I am totally OK with my repositories having more than one
commit tagged with a *prerelease* version: the information embedded into build
outputs will clearly indicate a [YMMV] situation.

[YMMV]: https://dictionary.cambridge.org/us/dictionary/english/ymmv

But, this practice exposes something that feels like a weakness in the [semver]
standard to me. [Semver] supports *prereleases* like `1.0.0-beta.1`, but it
doesn’t support “postreleases” — i.e., some way of expressing “this is something
that comes after version 1.0.0 but isn’t yet the next official release.”
Obviously there’s a symmetry here, but in my experience — and *definitionally*
if I’m rigorously adhering to semver semantics — I don’t know what the next
version number should be until I’m ready to make the release. After 1.0.0, my
next primary release might be 1.0.1, or 1.1.0, or 2.0.0, depending on what level
of API compatibility is maintained — so what do I choose to bump to? Maybe you
think you can plan carefully enough that you know what version will be next, but
I have no such confidence.

The semver standard does provide an “out”. From my reading of it, there are no
compatibility guarantees between primary releases and subsequent prereleases:
if I bump to `1.0.1-dev.0` after `1.0.0`, there can be API breaks and it’s OK
if the next full release is `2.0.0`, or `1.0.1` if the breaks are reverted.
So, we have a workable path in these cases … but I still don’t love it. (And
there’s the superficial issue that semver prereleases are sorted
lexicographically, so `1.0.1-dev.0` comes ”after” `1.0.1-beta.0`. This isn’t
foundational, but `dev` is the tag that I’d prefer to use for this kind of
prerelease.)


# Problem 2: Automation

It took me an embarassingly long time to be able to put my finger on the
second major thing that bothered me about my release and versioning workflow.

The problem is exemplified by [the release process script][wdf-release] that I
developed for the [wwt_data_formats] package. It tries to be thorough and
error-resistant. And it’s 16 steps long! This is silly — this is exactly the
kind of workflow that should be automated.

[wdf-release]: https://github.com/WorldWideTelescope/wwt_data_formats/blob/master/RELEASE_PROCESS.md
[wwt_data_formats]: https://github.com/WorldWideTelescope/wwt_data_formats/

While the *decision* to make a primary release should be made by a person, I’ve
convinced myself that there’s no reason not to automate the release activities
as aggressively as possible. I feel like I had some mental block about doing so
for a long time, and to be honest I’m not quite sure why. One reason, I think,
is that my release workflows necessarily involve activities like editing
`setup.py` files to insert version numbers, and I haven’t really liked the idea
of CI/CD pipelines making modifications to the Git repositories that they build.
But I guess I got over that discomfort at some point. Automate all of the
things!


# A First-Draft Automation Workflow

If I were to conjure up an automated release workflow that made a point of
solving the versioning-between-releases problem, what would it look like?

My first thought was that the core functionality might look like this:

- In “steady state”, the main development branch (which I’ll call `master`
  here) is versioned with a prerelease number, say `1.2.3-dev.0`.
- When it’s time for a release, I invoke a tool that:
  1. Edits the project files to the primary-release version number, 1.2.3.
  2. Commits the changes
  3. Creates a corresponding Git tag
  4. Edits the project files to the next pre-release version number,
     `1.2.4-dev.0`.
  5. Commits these changes
- When I push the commits and tag to GitHub (or whatever), the tag triggers a
  CI/CD workflow that executes release activities such as uploading to PyPI or
  what-have-you.

Graphically, the release commit history will look like:

```
  C (v1.2.4-dev.0[+0])
  |
  B (@v1.2.3) -- tag push triggers release pipeline
  | 
  A (v1.2.3-dev.0[+N])
```

where the chronological ordering is ABC, the `[+N]` annotation indicates that
this is the N'th commit annotated with that version number, and the `@`
annotation indicates that the version is marked with a Git tag, not just the
version numbers embedded in files like `setup.py`.

I’ve written this assuming the non-monorepo case where the repository contains
just a single versionable project (a … single-repo?), but you could extend it to
the monorepo case pretty straightforwardly. Likewise, I assume a semver
versioning model, but other models will have analogues.

I think this vision has weaknesses, though. For one, I don’t love the strategy
of using the next semver prerelease for the development version. That’s a pretty
minor complaint, and I could get over it if everything else felt right.

The big issue is that if the CI/CD of the release fails, I need to go back and
rewrite repo history, and maybe delete and recreate tags, in order to re-trigger
the release workflows. If the CI/CD pipeline is running on every commit to
`master` the odds of failure are small, but I strongly prefer a system where it
will simply never be necessary to rewrite history on the `master` branch. Since
we can only be sure if a commit is “release-worthy” by running it through the
CI/CD pipeline, *the decision to bless a particular commit as corresponding to a
release has to occur inside the CI/CD pipeline*. Hmm!

Finally, I’m a bit bothered by the Git two-step of committing the version
number bump and then immediately re-bumping it. That doesn’t feel right. The
most significant practical impact that I can think of is that it triggers a
few superfluous CI runs, which is far from the end of the world. But it feels
like I’m not using Git the way it’s meant to be used.


# The `rc` branch

Let’s run with this idea about only being able to approve a release inside the
CI/CD pipeline. If we take that as a constraint, the workflow has to involve
some sort of “nomination” step where I propose that a certain commit should
serve as the basis for the next release. Then, the CI/CD pipeline applies the
candidate version number(s), tests whether that commit succeeds and, if it does,
executes the release processes.

Over time, I’m going to nominate a sequence of commits from `master`, and the
nominated commits are always going to move forward in the Git history. That’s a
branch!

We can call this the `rc` (release candidate) branch. When I’m ready to make a
primary release, I push a commit from `master` to `rc`. CI/CD magic happens, and
in the end I hopefully get a release out. If not, I fix the problem on `master`
and merge the the fix to `rc`. In the simplest case, all updates to `rc` are
fast-forwards that catch it up with `master`.


# Decoupling the main branch from versions

If we decide to release through an `rc` branch, a new problem arises. When and
how do we update version numbers on `master`? You could automate it, but it
would be pretty annoying to have to add a new commit to `master` that updates
the developmental version numbers every time you make a release.

I propose that we just … not do that. On `master`, set every version number to
`0.0.0-dev.0` (or its equivalent), and keep it there forever. I can see how this
might feel like an offensive hack to some people, but something about this
approach actually feels very correct to me. I really like the idea of the
`master` branch moving forward without having to pay any mind to the particular
points at which releases are boxed up and shipped off.

This approach turns out to create some headaches — more on those below — but I
think they’re surmountable in a reasonable way.


# Applying version numbers — the `releases` branch

A few paragraphs up I wrote that the CI/CD pipeline “applies” version numbers
when processing an `rc` commit. That was a bit vague. Let’s flesh out this
process.

The core of this procedure is, literally, editing your `setup.py` or
`package.json` files and replacing the 0.0.0’s with actual version numbers. This
was another sort of “aha” moment for me — my [release recipes][wdf-release] all
involve editing various files to update their embedded version numbers, and *of
course* an automated tool should be doing that editing instead of me.

If we have to edit the files in the repository to appropriately set them up for
release, we of course need to make a Git commit preserving those changes, and to
preserve that commit somewhere. Now, a Git tag doesn’t need to point to a commit
that’s associated with any particular branch, so we could preserve the release
commits as branch-less “stubs” away from the mainline development:

```
  B (v0.0.0-dev.0[+N+1], master)
  |
  | A* (@v1.2.3)
  |/
  A (v0.0.0-dev.0[+N], rc)
```

Here, the commit A* does not appear in the history of any branch in the repo.
This is OK, but I don’t love it, and I also kind of like the idea of there being
directly traceable history between releases. (That is, that all commits in the
Git history of release `X.Y.Z` are contained in the Git history of release
`X.Y.(Z+1)`.) We can achieve that by adding another utility branch called
`releases`. Version-tagged commits will be forcibly merged into this branch,
like so:

```
                                B* (@v1.2.4, releases)
                               /|
                              / |
(v0.0.0-dev.0[+N+1], master) B  |
                             |  |
                             |  A* (@v1.2.3)
                             | /
                             |/
                             A (v0.0.0-dev.0[+N], rc)
```

When the commit B* is constructed, the actual file contents of A* are ignored —
we’re more indicating that B* is semantically the “successor” of A*.

In practice, we want to be running this merge-and-apply-versions operation all
the time, not just when primary releases are made. But that’s no problem: we can
perform this step in all CI/CD runs, but just not actually run any release
processes or update the `releases` branch unless the operation is being run on
the `rc` branch.


# The Monorepo Case

One of the original motivations for all of this thinking was that I’m finally
working with monorepos in earnest. Obviously, I wouldn’t have written all this
up if I didn’t think that this workflow could work in a monorepo paradigm. But
it definitely make things more tedious.

My initial investigations into this area centered on [Lerna], which seems to be
the standard JavaScript monorepo management tool. My thinking about how to
handle monorepos was kicked off by looking at Lerna’s design, so my assumptions
are probably pretty strongly influenced by its architecture.

[Lerna]: https://lerna.js.org/

To extend this versioning workflow to work with monorepos, you have to add some
wrinkles:

- Instead of one package with one version number in a repo, you have lots of
  packages each with their own version number. Lerna has a “non independent”
  mode where each package is assigned the same version number, but my instinct
  is that this is inappropriate for most cases, especially semver ones.
- Most other characteristics of the system vectorize over packages in the
  sensible way. For instance, instead of having a single set of tags `vX.Y.Z`,
  you have more tags including the name of each package, `$packagename@X.Y.Z` or
  similar.
- However, packages within the monorepo can have internal dependencies that form
  a [DAG] structure. Some operations have to care about this internal dependency
  structure.
- We can associate each package with a particular directory within the repo, and
  say that commits affecting any files in that directory are considered to
  affect that package. This paradigm isn't fully general, of course, but it
  probably suffices in the vast majority of cases.

Thus far, I’ve encountered three areas where the monorepo case has particularly
tricky interactions with the scheme I’ve been describing.

First, release deployment in the CI/CD pipeline. If a repository contains just
one package, it is fairly straightforward to write a linear CI/CD script that
builds artifacts, runs tests, and deploys if a release is successful. In a
monorepo, each package in the repo might have its own deployment stages, and any
arbitrary combination of packages might be getting released at any one time, and
some subset of those release processes might fail midway through. You need some
mechanism to track state about what’s getting released and conditionally invoke
the right steps. This is certainly possible, but it’s a lot more tedious.

Second, we need to do something fancier with the `rc` branch because we now need
to be able to indicate *which* packages are intended to be released. One option
is to reject the premise, and always make new releases of any package that has
changed since the last push to `rc`. This could work, but I don’t love it.
Alternatively, there’s no strong reason that every commit on the `rc` branch has
to also appear in `master`, so you could include information about release
intentions in a commit message or some kind of metadata file. In particular, my
current thinking is that pushes to `rc` could add changelog files — an update to
the changelog of a particular package would indicate an intention to release it.
I find this appealing since it also provides an opportunity for the changelog to
be manually edited. Some systems like [Lerna] always autogenerate changelogs,
but I think the ideal workflow would allow human revision of an autofilled
template.

Note that, if we’re including extra information indicating release intentions
when we’re committing to the `rc` branch, we could just ditch the `rc` branch
altogether and express our nominations when merging to `master`. I haven’t
decided how I feel about that, but it would simplify things a bit.

Third, version constraints on internal dependencies. If a monorepo contains
packages `foo_bin` and `foo_lib`, and `foo_bin` depends on certain versions of
`foo_lib`, how do we express that dependency?

We can’t write out a dependency on an actual released version number in the
`master` branch, because each package is labeled with the same `0.0.0-dev.0`
version. The internal dependencies won’t be satisfiable in an unmodified
checkout, which is a non-starter. So, in `master`, we have to write that
`foo_bin` depends on `foo_lib = 0.0.0-dev.0`, or something equivalent.

Unfortunately, you can’t automate the computation of internal version
constraints either. Say that at the HEAD of `master`, `foo_bin` and `foo_lib`
are both about to be released at version 1.4.0. Now, we can assume that in any
given checkout of the repo, the code in `foo_bin` is compatible with whatever
version of `foo_lib` comes alongside it. (That’s the whole point of a monorepo,
in a way!) But what other versions is it compatible with? Maybe it requires a
feature that was introduced in `foo_lib` 1.2.0, so that’s the minimum acceptable
compatible version. Or maybe it’s compatible all the way back to to `foo_lib`
1.0.0. This information is semantic and can’t be rederived automatically, in
general. It has to be codified in the monorepo somewhere in order for the
release tool to generate appropriate packaging metadata.

One solution to this problem would be to encode this information in a separate
metadata file and have the versioning tool transcribe it into the packaging
files when needed. This would probably work fine in practice, but it feels to me
like this approach is breaking an abstraction layer, and I think there’s a way
to do better. Because everything is in the same repo, we can refer to different
versions of sibling packages with *commit identifiers* rather than version
numbers. When release time rolls around, the versioning tool can consult the Git
database and translate the commit IDs to actual version numbers. This feels like
a good solution to me because it would be able to nicely flag a situation that
pops up sometimes: you want to make a release of `foo_bin`, but you have to
release `foo_lib` first, because of a required new feature that hasn’t yet made
it to a primary release.

To get even trickier, imagine a case where we are making a breaking change in
`foo_lib` and adapting to it in `foo_bin`. Such modifications should ideally
happen inside a single Git commit, if we like the idea of all commits in the
project history being buildable. But we need to update the metadata of `foo_bin`
to record that it now depends on the latest `foo_lib` … inside the commit that
is itself updating both of these packages. How do we name that commit before
we’ve created it? My solution is to use `git blame` functionality — we can use a
special identifier to indicate that the relevant commit is the very one that
last updated the line giving the dependency version specification. It can
contain a timestamp to disambiguate multiple successive updates to the same
line. This may start to feel like hacks piled upon hacks piled upon hacks, but I
think it all hangs together. Obviously, tooling automation would be important to
provide a smooth developer experience for these kinds of operations.


# Implementing it all

There are several release automation tools like [Lerna], [semantic-release], and
[versioneer]. Unfortunately, I don’t think that any of them fully meet my needs.

[semantic-release]: https://github.com/semantic-release/semantic-release
[versioneer]: https://github.com/warner/python-versioneer

The most common issue is that many of these tools only work with one language or
packaging system, while I want to apply my workflow for packages for JavaScript,
Python, and Rust *at a minimum*. Sometimes that will even be in the same
repository: for instance, the [pywwt] repo includes both a Python and a
JavaScript package, as do repos for many other elements of the [Jupyter]
ecosystem.

[NPM]: https://www.npmjs.com/
[pywwt]: https://github.com/WorldWideTelescope/pywwt/
[Jupyter]: https://jupyter.org/

I also need to be able to easily run the release automation tool on my personal
machine, and on CI servers, across the major platforms, since my projects often
need full platform coverage and the first step of the CI/CD pipeline will always
be to run the version-assignment operation.

So, you guessed it: we need a new [Rust CLI] tool!

I’ve started creating this new tool, called [cranko]. The name aims to suggest
that it’s helping you drive a conveyor belt of releases that’s always humming
along, swiftly and smoothly. It also resembles that of the wonderful Rust
package manager [cargo], although it can’t hurt to emphasize that [cranko] is
intended for use with all languages, not just Rust.

[Rust CLI]: https://rust-cli.github.io/book/index.html
[cranko]: https://github.com/pkgw/cranko
[cargo]: https://doc.rust-lang.org/cargo/

Before getting to serious work on [cranko], I decided to write up this document
to help clarify my thoughts, so there is virtually no code in the repo right
now. But, I do feel as if my thoughts are indeed clarified quite well now, so I
am hopeful that progress will be quick! The next big challenge will be to see if
this workflow works out as well as I envision. I’ve been making software
releases for a long time, so I think that I understand the problem space pretty
well — but a lot can happen in the space between naming a problem and solving
it. Stay tuned.

# The PKGW Versioning Workflow: TL;DR

- The release deployment process must be fully automated.
- On the main development branch (`master`), everything is always labeled with
  version 0.0.0.
- The first stage of the CI/CD pipeline is always to run an automated tool that
  creates a commit updating the project files (`setup.py`, etc.) with the actual
  version numbers that the next release(s) would have.
- Commits on the main branch are explicitly “nominated” for release, potentially
  by pushing them to an `rc` branch.
- If CI passes for a release-nominated commit, new releases are deployed and the
  new commit with actual version information is tagged and merged into a
  `releases` branch.
- In a monorepo, intra-repo dependency versioning needs special attention, but
  can be handled.