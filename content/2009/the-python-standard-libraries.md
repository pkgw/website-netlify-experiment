+++
date = 2009-11-28T15:33:38Z
title = "The Python Standard Libraries: Not Very Good"

[extra]
wp_rel_permalink = "/2009/11/the-python-standard-libraries/"
wp_shortlink = "/?p=174"
+++

Thomas Vander Stichele, whom I have never met but works in some of the areas
of Linux that I used to be involved with, [writes
about](http://thomas.apestaart.org/log/?p=1081) some ugly code he found in the
Python standard libraries, and says  > I usually tend to think of Python as
the discerning gentleman’s programming language: well-behaved, well-
documented, people take care of the code written. I like the batteries-
included approach and assume that the battery code in the standard library is
well-written…  I have to say that I have no idea what he’s talking about. The
Python standard libraries are _terrible_. Everywhere you look there are
inconsistent APIs and coding styles, redundant or missing functionality,
widely ranging quality in the documentation, and poorly-engineered solutions.
Consider the description of the [subprocess
module](http://docs.python.org/library/subprocess.html):  > … This module
intends to replace several other, older modules and functions like: >  > *
os.system > *   os.spawn\* > *   os.popen\* > *   popen2.\* > *   commands.\*
That is, the Python standard libraries contain at least _four_ different APIs
for invoking subprograms, and I have to say that I still don’t think latest
iteration is great. The os module, which provides core functionality,  just
exposes the standard POSIX API without making any efforts to map it into the
language helpfully or abstract very well for non-POSIX systems. Google
indicates that urllib is pretty widely hated. StringIO vs cStringIO, pickle
vs. cPickle, about a dozen different database and XML modules … it’s a mess.
Now, of course, this is all just saying that the Python standard libraries are
what they are: they were written by many different people in many different
styles at different times, and they were developed quickly to get
functionality out there so people could use it. I think that _is_ very
Pythonic: Get Stuff Done and if not everything is perfect, so be it. But I
have to say, it’d be nice if the standard libraries were better. They’re
bread-and-butter APIs, and it would, you know, be nice if they were carefully
and thoughtfully designed. The fact that they aren’t turns out not to be a
deal-breaker, but it remains unfortunate.
