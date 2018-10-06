+++
date = 2016-07-21T13:58:13Z
title = "Code, Copyright, and Licenses: The Bare Minimum You Should Know"
path = "2016/07/code-copyright-and-licenses-the-bare-minimum-you-should-know"

[extra]
wp_rel_permalink = "/2016/07/code-copyright-and-licenses-the-bare-minimum-you-should-know/"
wp_shortlink = "/?p=992"
+++

(_OK, I thought this was going to stay short, but it didn’t. For the
[tl;dr](https://en.wikipedia.org/wiki/TL;DR), scroll down to **Rhetorical
question #2**._)

More and more astronomers are publishing the source code to the software that
they write, which is awesome. Usually, though, we’re pretty sloppy about the
legalities associated with publishing code. And who can blame us? That stuff
is annoying and boring, right? Well … I actually think the relevant law is
kind of interesting, to be honest. But even if you’re not like me, it’s
important to cover your legal bases if you want other folks to use your code.
Fortunately, there are only a few core concepts to understand, and to “cover
your bases” you only need to do a few simple things. I’ll try to explain the
whys and hows below. Keep in mind that _I am not a lawyer, this is
not legal advice, etc._

**Fact #1.** _If you just ignore the legal stuff, it will be illegal for
anyone else to use your software!_ This is why you should keep reading! Of
course, scientists have ignored the legalities and used each other’s software
since software was invented. But it barely takes any effort to do better, and
there are more and more cases where you can’t just ignore these things — think
of multi-million-dollar international scientific collaborations with boards
and MOUs and all that jazz. Unless they can prove that it is legal for them to
use a certain piece of code, they won’t touch it. So, why is Fact #1 true?
Let’s start with one little piece of theory. It’ll be quick, I promise.

**Fact #2**: _Copyright is how we express “ownership” of intangible creative
works._ We have an intuitive sense of what it means to be the owner of
tangible property, something like a paperback book. But what does it mean to
“own” something intangible, like the novel you just wrote? You could answer
that question in a lot of ways (such as by rejecting its premise). But in our
legal system, when it comes to things like novels, we have a copyright system:
each work has a sort-of owner, the “copyright holder,” that has the sole right
to, well, make copies, in a broadly construed sense: to print a novel in book
form, to let someone make a movie out of it, and so on. I own a printed
paperback copy of
[Under the Volcano](https://en.wikipedia.org/wiki/Under_the_Volcano), but the
estate of
Malcom Lowry (probably) owns Under the Volcano, the novel.

OK. End of theory. **Fact #3**: _(Essentially) every creative work in the US
is copyrighted._ Under current law, if you produce any creative work — paint a
painting, write an article, take a photo, develop some software — it is
_automatically_ copyrighted, and you are the copyright holder. (Well, yes,
there are exceptions, but this is a good rule of thumb.) And, therefore, if
you care to assert your legal rights, no one else is allowed to reproduce your
work without your permission.
[Tweets are likely not copyrightable](http://www.canyoucopyrightatweet.com/)
but just about anything more substantial is.

**Fact #4**: _You have to assume that creative works are copyrighted._ This is
why Fact #1 is true: if I find some random piece of code on the internet, I
have to assume that it’s copyrighted. Even if I don’t know who the copyright
holder is, I’m not allowed to reproduce it: “All rights reserved” is the
default. Which means I can’t save it to my computer, and I can’t include it in
my own software … I basically can’t do anything with it.

(Is it good that everything is automatically copyrighted and thus not
reproducible by default? I personally think it’s terrible! I also think that
intellectual property law is _hugely_ important to our culture in ways that
99% of people just don’t perceive. For instance, a huge mass of cultural
artifacts out there are “orphaned” because we don’t know or can’t find the
copyright holders, and so _no one_ is legally allowed to copy them. As it is,
the relevant law is basically written by big corporations — copyright terms
have been getting retroactively extended for decades basically because Disney
will do everything it can
[to prevent Mickey Mouse from entering the public domain](https://www.eff.org/deeplinks/2016/01/well-probably-never-free-mickey-thats-beside-point).
But, regardless of what _should_ be, this is how things _are_.)

Well, there must be a way to make things less restrictive, right?
Indeed. **Fact #5**: _Copyright holders can distribute their works with
“licenses” that grant you rights you wouldn’t ordinarily have, including the
right to reproduce._ This is the key. The license is kind of like a take-it-
or-leave-it contract that’s automatically offered to anyone coming into
possession of a copy of your creative work. Typically, it says that if they
meet conditions XYZ, you grant them the rights to do ABC with your work. For
instance: “I generously grant you the right to make one personal copy of this
nice photo … if your name is Steve, and it’s a Thursday. And you can’t show
your copy to anyone else.” If you don’t like the conditions, then the default
rules apply: all rights reserved. The copyright holder can distribute their
work with whatever license they want.

So: **If you want people to be able to use your code, it has to come with a
license.** Otherwise, legally speaking, they have to assume that “All rights
reserved” applies. This leads to …

**Rhetorical question #1**: _How do I figure out what to put in my license?_
Just use one that’s already been written! There are literally dozens of
licenses specifically designed for software — different ones grant different
rights and impose different conditions. This turns out to be an area where
Open Source / Free Software nerds have endless, pointless, depressing internet
flamewars. Just
[Google “GPL sucks”](https://www.google.com/search?hl=en&q=gpl%20sucks&safe=active)
or something to get a taste. While I personally believe that these things
really do matter and are worth debating, there are only so many hours in the
day. For various Linux-nerd reasons I feel bad for saying this, but: just use
[the MIT License](https://opensource.org/licenses/MIT). It’s short and
reasonable.

**Rhetorical question #2:** _OK, amateur-hour internet lawyer guy … **what do
I actually do?**_ I recommend that you do this:

1.  _For every single software project that you make public in any way,_
  include a file in the top directory named LICENSE.txt that includes the text
  of your license of choice.
2.  _For every single non-trivial source code file that you make public in any
  way,_ include a two-line header comment of this form:

  ```
  # Copyright 2016 Your Name <your@email>.
  # Licensed under the MIT License.
  ```

[You can do more](https://www.gnu.org/licenses/gpl-howto.en.html), but I feel
that this is the safe minimum. It’s important to include the copyright /
license summary in every single file because people will extract files from
random projects willy-nilly, and they are almost never good about preserving
provenance information. These two lines provide the key information: who owns
the copyright, how to contact them, and what the license is. If you’re in a
non-small collaboration you could assign the copyright to the collaboration;
this is probably a bit iffy from a legal standpoint, but it provides more of a
feeling of communal ownership than a proclamation that “this file is mine!”,
which is probably more important than legal iffiness unless you think there’s
a significant chance that lawyers are actually going to get involved in
whatever it is you’re doing.

**Rhetorical question #3:** _Does this stuff affect anything else I do?_ You
betcha! You know those copyright assignment forms that journals have you
submit to them? Or the license terms that [arxiv.org](http://arxiv.org/) makes
you choose from? Ever seen things annotated with
[Creative Commons licenses](https://creativecommons.org/licenses/)? Your
papers are also copyrighted creative works. Hopefully you’re now armed with
some insight that will help you think abot what’s going on when you assign
copyright, choose an Arxiv license, etc.

**Rhetorical question #4**: _Gosh, this is all so fascinating, how can I learn
more?_ Innumerable pixels have been spilled discussing these topics, so just
try Googling a bit
([e.g.](https://www.google.com/search?hl=en&q=copyright%20law%20introduction&safe=active)).
The [Free Culture Foundation](http://freeculture.org/) is a go-to for learning
about why copyright is so important to our society in general. The
[Choose-a-license website](http://choosealicense.com/) describes software
license tradeoffs in a non-inflammatory way. The
[Creative Commons licenses](https://creativecommons.org/licenses/) are kind of
like open-source licenses for non-software works.
