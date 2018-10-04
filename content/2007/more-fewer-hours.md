+++
date = 2007-08-30T00:44:13Z
title = "More Fewer Hours"

[extra]
wp_rel_permalink = "/2007/08/more-fewer-hours/"
wp_shortlink = "/?p=7"
+++

Another day in which I just wasn’t able to put in that many hours, since I had
two separate friends who happened to be in town that I spent time with. The
time that I did spent was towards the data analysis for the 120 photometry
lab. I wrote a quick, 80%-useful module to display an ndarray, and used it to
check that my flatfielding code was working more or less correctly. After some
consultations with the redoubtable JohnJohn, I think that I can generate
trustworthy flat frames.  My next step is to locate stars in the science
frames. I _think_ that I can do this relatively well (via point-and-click user
interaction) without too much effort, but given that the stars don’t move
around too much, I could probably do it a lot more quickly manually. A simple
cursor-location feedback system would be enough for a first cut. Then, I need
2D Gaussian fitting to get the star locations more precisely. Hopefully numpy
or scipy has something to do this; I don’t want to translate gaufit2d.pro from
IDL into Python.  Once that’s all done, I think I can bang out the aperture
photometry in a day, if it’s as simple as I think it ought to be.  Maybe I
should switch over from this work back to ATA stuff, though. I don’t have the
clearest idea of what my next step with that data should be, though. I should
consult with Geoff (Bower) about that.  Third consecutive night at which I’m
in Campbell past midnight. But, in my defense, in all three cases it’s been
because I’ve been out with people late and have just needed to pick up my bike
before going home. Once all my stupid friends stop being in the stupid Bay
Area, this kind of thing will come to a stop. I hope.
