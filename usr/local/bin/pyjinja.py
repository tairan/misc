#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from jinja2 import Environment, FileSystemLoader, Template

def get_template_env(path):
    return Environment(loader=FileSystemLoader(path))


def output(dst, tpl):
    parent = os.path.dirname(dst)
    if not os.path.exists(parent):
        os.makedirs(parent)

    with open(dst, 'w') as f:
        f.write(tpl.render())


def main(src, dst):
    env = get_template_env(src)

    for name in env.list_templates():
        tpl = env.get_template(name)
        output(os.path.join(dst, name), tpl)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: {0} <template_dir> <output_dir>'.format(sys.argv[0]))
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])
