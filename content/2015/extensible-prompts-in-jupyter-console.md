+++
date = 2015-11-15T12:36:24Z
title = "Extensible prompts in “ipython” and “jupyter console”"

[extra]
wp_rel_permalink = "/2015/11/extensible-prompts-in-jupyter-console/"
wp_shortlink = "/?p=962"
+++

I use [IPython](https://ipython.org/) and sometimes the `jupyter console`
program for interactive Python work. (I used to think that the `ipython`
console program was getting deprecated with the advent of the Jupyter split,
but it turns out that that’s not the case.) When I do so, I like to customize
the input prompt that they show me. Unfortunately, it’s not well documented
how to configure custom prompts, and the method for doing so is **very**
different depending on which version of the software you’re using. Here’s my
compilation the relevant methods.

(This post has been heavily revised since its original version since I was
confused about the lay of the land, and was over-optimistic about IPython’s
stability. Last updated **2016/08**.)

**IPython, newer method (version >= 5.0):** IPython 5.0 uses a completely new
subsystem for gathering input: [prompt\_toolkit](https://python-prompt-
toolkit.readthedocs.io/en/latest/). So, the way to customize your prompts has
completely changed. Yay. To customize how prompts are generated, you need to
provide a customized version of a small class on IPython startup. Put code
like this in your `~/.ipython/profile_default/ipython_config.py` file:

```python
# This file is dedicated to the public domain.

try:
    from IPython.terminal.prompts import Prompts as BasePrompts
except ImportError:
    pass # not IPython 5.0
else:
    from pygments.token import Token
    from time import strftime

    class MyPrompts(BasePrompts):
        def in_prompt_tokens(self, cli=None):
            return [
                (Token.Prompt, strftime('%H:%M') + ' '),
                (Token.PromptNum, str(self.shell.execution_count)),
                (Token.Prompt, ' >>> '),
            ]

    c.InteractiveShell.prompts_class = MyPrompts
```

See the file `IPython/terminal/prompts.py` to see what else you can override
in the `Prompts` class.

**Jupyter Console, newer method (works on console version
4.1):** There’s no good approach, but there’s a hack. The key issue is that
under Jupyter, the “shell” that displays the user interface is a separate
program than the actual Python code you’re running. To customize the prompt,
you need to inject new code into the shell program, not the kernel. The
console _shell_ (again, not kernel) seems to load the config file
`~/.jupyter/jupyter_console_config.py`. You can inject some code into module
that renders prompts by putting something like this in that file:

```python
# This file is dedicated to the public domain.

from IPython.core import prompts
import time
prompts.lazily_evaluate['shorttime'] = \
  prompts.LazyEvaluate(time.strftime, '%H:%M')
c.PromptManager.in_template = '{shorttime} \\# >>> '
```

**Juypter Console, older method (console versions 4.0 and below?):** This
method must have worked for me at some point, but now I’m not sure how it ever
did. Anyway, the way you’re _supposed_ to inject code into Jupyter
applications is through the “extension” mechanism. Version 4.1 of the shell
can’t load extensions, but I guess older versions did. So you could install an
extension that set up the prompt renderer as follows.

First, you need to
create an extension by creating a file named something like
`~/.ipython/extensions/shorttime_ext.py`.

```python
# This file is dedicated to the public domain.

_loaded = False

def load_ipython_extension(ip):
    global _loaded

    if _loaded:
        return

    from IPython.core.prompts import LazyEvaluate
    import time
    ip.prompt_manager.lazy_evaluate_fields['shorttime'] = \
    LazyEvaluate(time.strftime, '%H:%M')
    _loaded = True
```

Then you can cause this extension to be loaded and modify the prompt of your
shell using the standard configuration framework. In the 4.0.x versions of the
console, the relevant file was still
`~/.ipython/profile_default/ipython_config.py`. A standalone version of that
file that would set things up is:

```python
# This file is dedicated to the public domain.

c = get_config()
c.InteractiveShellApp.extensions = ['shorttime_ext']
c.PromptManager.in_template = '{shorttime} \\# >>> '
c.PromptManager.in2_template = '{shorttime} {dots}...> '
c.PromptManager.out_template = '{shorttime}   \\# < '

# This suppresses 'Loading IPython extension: foo' messages on startup:
import logging
logging.getLogger('ZMQTerminalIPythonApp').level = logging.WARN
```
