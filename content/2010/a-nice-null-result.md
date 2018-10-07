+++
date = 2010-02-23T23:31:00Z
title = "A Nice Null Result"
path = "2010/02/a-nice-null-result"

[extra]
wp_rel_permalink = "/2010/02/a-nice-null-result/"
wp_shortlink = "/?p=190"
+++

[OkCupid](http://okcupid.com/) is a dating site that takes a pleasantly data-
driven approach to the online dating game. If you read
[their blog](http://blog.okcupid.com/), you run into a lot of interesting and
surprising facts that the OkCupid staff have pulled out of their databases.

Like many dating sites, OkCupid gives its users a list of questions to answer
about themselves. For each question, however, it also lets you specify what
your ideal partner’s response would be, and how important that response is to
you. (You might not always want your partner to have the same response as you
— for instance, “Are you sexually dominant?”) This lets OkCupid rate the
compatibility between two members _according to their personal standards_, not
just according to what the employees at OkCupid think makes for a good couple.

You can then do interesting aggregate statistics by breaking the users down
into groups and then looking at the average compatibility between different
groups. On
[this post](http://blog.okcupid.com/index.php/2009/10/05/your-race-affects-whether-people-write-you-back/)
on the OkCupid blog, they did various breakdowns and visualized the results on
grids like the one below. Each group has its own row and column, and the
intersection of a row and column gives the average compatibility between the
two groups. A greener color means above- average compatibility, and a redder
color means below-average compatibility. For instance, here are the
compatibilities of racial groups:

{% figure(path="wp/wp-content/uploads/2010/02/Match-By-Race.png") %}
Dating compatibility between racial groups, taken from blog.okcupid.com
{% end %}

This is somewhat heartening: in theory, people of all races should be able to
get along pretty well in relationships. (Unsurprisingly, in practice, this is
untrue. Different racial pairings on OkCupid reply to each other’s messages at
rates that vary wildly from what their compatibility scores would imply,
indicating that people’s personal attitudes affect things strongly. See
[the blog post](http://blog.okcupid.com/index.php/2009/10/05/your-race-affects-whether-people-write-you-back/)
for more info.)

Anyway, here’s that null result that I referenced in the title:

{% figure(path="wp/wp-content/uploads/2010/02/Match-By-Zodiac-Title.png") %}
Dating compatibility by zodiac sign, taken from blog.okcupid.com
{% end %}

From a sample of 500,000 users, 144 comparisons, all within 0.5% of the mean
value. That’s a null hypothesis that I can get behind.

(As a side note, the fact that OkCupid lets people rate the personal
importance of others’ answers to various questions allows them to easily
discover which questions are the most effective for testing compatibility.
Apparently “How often do you shower?” is one of the best.)
