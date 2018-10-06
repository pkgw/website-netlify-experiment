+++
date = 2014-08-27T17:20:33Z
title = "“A Laboratory Introduction to git”"
path = "2014/08/a-laboratory-introduction-to-git"

[extra]
wp_rel_permalink = "/2014/08/a-laboratory-introduction-to-git/"
wp_shortlink = "/?p=897"
+++

Earlier this summer I ran a tutorial for our new summer students on the
[git](http://git-scm.com/) version control system.

Last year, I also ran a git tutorial, but was only partially happy with the
results. I knew that I didn’t want to stand and lecture the students as a
group, since git is fundamentally a _tool_: there’s no better way to learn
about it than just to use it. But there are some important and subtle concepts
underlying how git works and I wanted to explain them. I found myself
lecturing more than I wanted, and I could tell that the Fundamental Problem of
Lecturing was rearing its head: my one-size-fits-all approach was not working
for everyone. Some students were interested, others not; some were following
the concepts, and others were confused. I felt like the tutorial worked very
well for a few students, but must have been boring, confusing, or frustrating
for others.

This year I spent some time thinking about how to do better. The idea that I
kept coming back to was that, in my experience, when you’re presenting
technical material, different people can absorb it at _very_ different rates —
to the extent that this should be the _dominant_ factor in considering how to
prepare a group learning experience. I decided that my key goal was to find a
way to let students learn the material at their own pace.

Almost immediately I realized that what I wanted to do was run my tutorial
like the lab section of a college science class. I’d write up the material in
handout that would (if I did a good job) demonstrate the key concepts with
hands-on activities. I’d pair up students so that they could help each other
out if they got stuck: basic
[peer learning](http://en.wikipedia.org/wiki/Peer_learning) in action, with a
whiff of [pair programming](http://en.wikipedia.org/wiki/Pair_programming)
too. Then I’d just tell the students to start reading and doing. Rather than
“leading” the tutorial, I and my co-teachers would be _lab assistants_, there
to step in when groups got really stuck.

The one downside of this approach that I could think of is that you can’t
extemporize a half-assed, poorly-structured handout the same way you can a
half-assed, poorly-structured lecture. That doesn’t seem like an entirely bad
thing, but  I did need to spend some solid time planning and writing the “lab
manual”.

The manual in question is
[here](https://newton.cx/~peter/files/git-lab-handout.pdf), with its
[full source code on GitHub](https://github.com/pkgw/git-lab). I was very
happy with what I put together. I’d like to think I explained the concepts
well, and I think the “lab manual” style ended up working out as well as I’d
hoped. Furthermore, I stole some font ideas from
[Michelle Borkin’s dissertation](http://dash.harvard.edu/handle/1/12274335)
(in turn borrowing from [here](https://github.com/aleifer/dissertation) and
[here](https://github.com/suchow/Dissertate)) and I think the resulting
document looks pretty snazzy too.
[Check it out!](https://newton.cx/~peter/files/git-lab-handout.pdf)

And I was extremely happy with how the tutorial went, too. As you’d expect,
some students got farther than others, but I don’t think anyone got
frustrated; the uninterested students can let themselves get distracted, and
the students that need some more time can take it. Another nice bonus of the
lab approach is that the students can hang on to the manual and use it as a
reference later. I **highly recommend** running technical tutorials in a 
“lab” style! You do need to plan ahead to make a manual, but, well, sorry,
sometimes it takes some work to make something you’re proud of.

I also highly encourage anyone to use or modify my git lab manual if they’re
planning any analogous activities. Of course, I’d appreciate hearing about way
to improve what I’ve got, say through a
[GitHub pull request](https://github.com/pkgw/git-lab/pulls).

I did come away with a few lessons learned from this first iteration, though:

- Many, if not most, students will hit an _immediate_ stumbling block with
  just trying to use and understand a Unix text editor. This pops up
  particularly early in my git tutorial but of course will come up rapidly for
  any kind of Unixy technical computing. (The Software Carpentry folks
  [encounter the same problem](http://f1000research.com/articles/3-62/v1).) As
  far as I can see it, right now there’s just no way to avoid this pain. Which
  is lame.

- I also tried early in the manual to establish simple conventions for “type
  this text _exactly …_ except for this one piece that I want you to replace,”
  but they were apparently not simple enough. I think that just a few more
  explicitly and _very_ gently introduced examples would help.

- Students ended up mostly working solo, rather than pairing, though they help
  each other out in sticky spots. I half-expected that this might happen; in
  general, you seem to need to exceed an _enormous_ psychological activation
  energy to actually get students to work together in a small group. I think
  doing a better job on this front is more about my teaching technique and
  presence rather than any concrete instruction I could give. It’s not too bad
  if the students at least help each other, but I still believe it’d be even
  better for them to work in pairs if I could convince them to.

- After giving the tutorial, someone pointed out that I didn’t have anything
  in place to evaluate the students’ learning. There are questions to answer
  in the lab manual, but it was clear that I wasn’t actually going to be
  reviewing their answers or anything. Obviously no one’s going to be grading
  them, but evaluation is important for understanding what’s working and what
  isn’t … and I do tend to think that that small  bit of pressure on the
  students from knowing that I’d be looking at their work would be a positive
  thing. Next time I might have them write the answers to my questions in a
  separate packet that I actually collect (while emphasizing that it’s about
  judging my teaching, not them).

- There are also a bunch of smaller things. I ask the students to run `man
  find`, which creates a pager, before telling them how to exit a pager. I ask
  them to type `rm -rf *` at one point which is probably just too dangerous.
  Not-quite-substitutions like `{edit the file foo.txt}` were confusing.
  Despite my best efforts to make the
  [bug in bloomdemo](https://github.com/pkgw/bloomdemo/blob/master/bloom.py#L121)
  _blazingly_ obvious, it was not for some people.

I’m looking forward to revising the manual next year and trying to do an even
better job!
