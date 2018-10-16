+++
date = 2015-02-01T00:00:00-04:00
title = "Debug PhantomJS Interactively"
weight = 0 # all howtos have zero weight => alphabetical ordering
template = "howto.html"
+++

Basic instructions are [here](http://phantomjs.org/troubleshooting.html) but
confused me for a while.

1. These steps may only work with phantomjs 2.0.1 or higher; cf
   [#12864](https://github.com/ariya/phantomjs/issues/12864).
2. The phantomjs driver script must be instrumented in two places. First, put
   a `debugger;` statement somewhere in the main driver. Second, add a line
   like this: 
   ```
   page.evaluateAsync (function () { debugger; });
   ``` 
   somewhere after the page has been created.
3. Launch the driver giving an extra argument `--remote-debugger-port=51515`
4. Open <http://localhost:51515/> in a Webkit browser. Phantomjs is
   Webkit-based, and its interactive debugger only works in Webkit too. So,
   basically, go use Google Chrome to view it.
5. There will be some bulleted list of links to click on, with the initial
   text possibly being empty. I.e., you may just see a single bullet. If so,
   view the page source and navigate to the link, which is something like
   <http://localhost:51515/webkit/inspector/inspector.html?page=1>.
6. Go to the console section and run the command `__run()`. This should switch
   over to the JavaScript debugger with the script paused, although the line
   numbering seems to be off so it doesn’t know where to show you that it’s
   stopped.
7. Open a new tab and go back to <http://localhost:51515/>. There should now
   be a second item in the bulleted list, and clicking on it will open a new
   inspector operating in the context of your webpage inside PhantomJS.
8. Go back to the initial tab and hit the *Continue* button.
9. In the second tab, the debugger should now be stopped at the breakpoint you
   set before. You should now be able to use all the standard inspector
   features, including debugging the DOM, etc.
