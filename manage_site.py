# Copyright 2018 Peter Williams <peter@newton.cx>
# Licensed under the MIT License.

"""Some Python utilities for programmatically manipulating the website
content.

"""
import sys
from pwkit.io import Path

root = Path(__file__).parent
content = root / 'content'

def all_blog_posts():
    "Generate the paths to the Markdown files for all blog post."

    for year in content.glob('2???'):
        for post in year.glob('*.md'):
            if post.name.startswith('_'):
                continue

            yield post


def read_markdown(path):
    """Read a Markdown file.

    Returns `(front_matter, content)`, where `front_matter` is the unparsed TOML
    text at the beginning of the file, and `content` is the main Markdown
    content. The "+++" delimiters do not appear in either.

    """
    path = Path(path)

    with path.open('rt') as f:
        line = f.readline()
        assert line == '+++\n'

        front_matter = []

        while True:
            line = f.readline()
            if line == '+++\n':
                break

            front_matter.append(line)

        front_matter = ''.join(front_matter)
        content = f.read()

    return front_matter, content


def rewrite_markdown(path, front_matter, content):
    "Rewrite a Markdown file with TOML front matter."

    path = Path(path)

    with path.make_tempfile(resolution='overwrite', mode='wt') as f:
        print('+++', file=f)
        print(front_matter, file=f)
        print('+++', file=f)
        print(content, end='', file=f)


# One-time operations

def insert_wp_paths():
    """A one-time operation: insert \"path =\" definitions in the front matter for
    the blog posts, to preserve the old Wordpress URLs.

    """
    import pytoml

    for path in all_blog_posts():
        fm_text, content = read_markdown(path)

        fm = pytoml.loads(fm_text)
        web_path = fm['extra']['wp_rel_permalink']
        if web_path[0] == '/':
            web_path = web_path[1:]
        if web_path[-1] == '/':
            web_path = web_path[:-1]

        fm_lines = fm_text.splitlines()

        for i in range(len(fm_lines)):
            if fm_lines[i].startswith('title ='):
                break
        else:
            raise Exception(f'no title in {path}?')

        fm_lines = fm_lines[:i+1] + [f'path = "{web_path}"'] + fm_lines[i+1:]
        fm_text = '\n'.join(fm_lines)

        rewrite_markdown(path, fm_text, content)
