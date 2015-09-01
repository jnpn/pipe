'''
A Python eDSL for Linux shell pipes.

2 implementations:
-----------------

  - OOP / classes
  - FP only

Example:
-------
'zw': [
        ['zcat', './archive.tar.gz'],
        ['grep', '-a', '-i', 'bogus'],
        ['wc', '-l']
    ]

will be equivalent to:

    `zcat ... | grep ... | wc -l`
'''

import click
import json

from fp import pipe, com, show
from oop import Beg, End

from config import PIPES


def fp(p):
    '''
    Function based code: Pipe -> String, Value

    f: the shell representation of the pipe 'a | ... | z'
    r: the value returned by the OS.
    '''
    f = show(p)
    r = com(pipe(p))
    return f, r


def oo(p):
    '''OOP wrapper based code.'''
    beg = Beg()
    end = End()
    for cmd in p:
        beg | cmd
    r = beg | end
    return beg, r


@click.command()
@click.option('--kind', type=click.Choice(['fp', 'oo']), default='fp')
@click.option('--cmd', multiple=True, type=str)
def do(kind, cmd):
    machinery = globals()[kind]
    print(machinery.__doc__)

    cmds = [json.loads(c) for c in cmd]
    pipes = cmds if cmds else PIPES.values()
    for p in pipes:
        f, r = machinery(p)
        print(f, '->', r)

if __name__ == '__main__':
    # $ diff -y <(python pipes.py --kind oo) <(python pipes.py --kind fp)
    do()
