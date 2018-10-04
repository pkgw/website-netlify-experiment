+++
date = 2012-12-28T14:56:55Z
title = "Silence is Golden"

[extra]
wp_rel_permalink = "/2012/12/silence-is-golden/"
wp_shortlink = "/?p=622"
+++

Scientists _love_ to write programs that are too chatty.  Chatty programs are
eager to tell you what they’re doing and how they’re doing it. On the command
line, this means you get a lot of output:  $ ./run-simulation.py input.dat
output.dat Science simulation by Peter Williams Opening the input "input.dat"
...    ... 300 items Running simulation! Step 1 DEBUG: n=12 Step 2 Step 3
Opening "output.dat" for writing ... All done! $  Contrast this with classic
Unix tools, where silence implies success:  $ cp source.txt destination.txt $
There are a lot of reasons why people write chatty programs: some good, some
at least understandable. But I want to suggest that chattiness is something to
be _actively fought_.  One concrete issue is that it’s hard to notice when
chatty programs have problems. Showstopping errors are generally easy to pick
out because they’ve, well, stopped the show, but I can’t tell you how many
times I’ve missed some important warning message because it got scrolled off
the screen by a bunch of inane diagnostics. And beginning programmers — which
is what most scientists are — generally have trouble writing error-handling
code and often write programs that charge ahead past conditions that _should_
be showstoppers.  Less concretely but just as importantly, chatter is
_distracting_. When I’m using a computer, I’m trying to get stuff done, and I
get more done when I’m not wasting time thinking about low-level details: I’m
in a line of work where _my attention is one of my most valuable resources_. A
chatty program is like a needy employee who can’t make progress without coming
back to you over and over for handholding and reassurance. _Just do what I
asked and stop bothering me unless you run into a problem you can’t solve._
When I need to move files around in the terminal, I can bang out commands and
I just _know_ that everything is OK because I’m not seeing any messages. I
have to stop and _read_ the output of my simulation to see if it went wrong.
My advice is look at every line your program prints and ask yourself, _do I
really care?_ Vital outputs should be respected by not being surrounded by
chatter, or by being recorded to disk instead of left to scroll off the
terminal screen. _Diagnostics should be separate_: either optional and off by
default, or output in some secondary way so that the “main” output is clean.
Always keep in mind that every unhelpful message is drawing your precious
attention away from the important ones.  For the beginners out there, I’d
argue that reducing chatter also helps build confidence. One tends to have
this irrational fear that the program _usually_ works but maybe this time it’s
derailed in some crazy way and is producing garbage. Seeing the same output
over and over again is reassuring. But take those training wheels off! If
you’re seeing the same output over and over, by definition you’re not learning
anything new. To be confident in quiet programs, you do have to evaluate which
parts of your program are the most likely to go wrong, and you do need to get
good at handling error conditions. _These are vital skills for competent
programming_, and the faster you develop them, the better.
