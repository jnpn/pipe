import click
import collections
import json
from subprocess import PIPE, Popen

# def pipe(ps):
#     pps = []
#     p0, *ps = ps
#     last = Popen(p0, stdout=PIPE)
#     pps.append(last)
#     for p in ps:
#         print(last.args, '<', p)
#         _ = Popen(p, stdin=last.stdout, stdout=PIPE)
#         last.stdout.close()
#         pps.append(_)
#         last = _
#     return pps

from functools import reduce

# [Pi]
# [Pi, Pj(Pi)]
# [Pi, Pj(Pi), Pk(Pj)]

# def pipe(ps):

#     def _(a, p):
#         so = lambda a: a[-1].stdout
#         P = Popen(p, stdin=so(a), stdout=PIPE)
#         so(a).close()
#         A = a.copy()
#         A.append(P)
#         return A

#     hd, *tl = ps
#     pp = reduce(_, tl, [Popen(hd, stdout=PIPE)])
#     return pp

# def pipe(ps):

#     def uno(p):
#         return Popen(p, stdout=PIPE)

#     def duo(a, p):
#         so = lambda a: a[-1].stdout
#         P = Popen(p, stdin=so(a), stdout=PIPE)
#         so(a).close()
#         return P

#     def ext(l, e):
#         L = l.copy()
#         L.append(e)
#         return L

#     hd, *tl = ps
#     pp = reduce(lambda a, p: ext(a, duo(a, p)), tl, [uno(hd)])
#     return pp

def pipe(ps):

    def uno(p):
        return Popen(p, stdout=PIPE)

    def duo(a, p):
        *_, last = a
        P = Popen(p, stdin=last.stdout, stdout=PIPE)
        last.stdout.close()
        return P

    def ext(l, e):
        L = l.copy()
        L.append(e)
        return L

    hd, *tl = ps
    pp = reduce(lambda a, p: ext(a, duo(a, p)), tl, [uno(hd)])
    return pp

def com(pipes):
    pipes[0].stdout.close()
    return pipes[-1].communicate()[0]

def mapc(f, l, s=' '):
    return s.join(map(f, l))

### FONADIC
### BUG: fails with pipe of length one

class StartPipe:

    def __init__(self, ):
        self.cmds = []

    def __neg__(self, ):
        self.cmds = []
        return self

    def __or__(self, cmd):
        # if cmd is None or cmd is self:
        #     return com(pipe(self.cmds))
        if type(cmd) is EndPipe:
            return cmd._(self.cmds)
        else:
            self.cmds.append(cmd)
            return self

    def __repr__(self, ):
        return mapc(str, self.cmds, ' | ')

class EndPipe:
    def _(self, cmds):
        return com(pipe(cmds))

## Helpers

def fp(p):
    '''Function based code.'''
    f = mapc(str, p, ' | ')
    r = com(pipe(p))
    return f, r.decode('utf8')

def oo(p):
    '''OOP based code.'''
    beg = StartPipe()
    end = EndPipe()
    -beg
    for cmd in p:
        beg | cmd
    r = beg | end
    return beg, r.decode('utf8')

PIPES = collections.OrderedDict({
    'lgs': [
        ['ls', '-a', '/home/agumonkey/'],
        ['grep', 'bash'],
        ['sed', 's, bash, BASH, g']
    ],
    'es': [
        ['echo', 'foo bar baz'],
        ['sed', 's, , @@@, g']
    ],
    'ps': [
        ['echo', 'foo bar baz'],
        ['sed', 's, , | , g']
    ],
    'wat':[
        ['echo', ' oob rab zab'],
        ['sed', 's, b, b\\n, g'],
        ['sed', 's, \(.*\), >>> \\1 !, g']
    ]})

@click.command()
@click.option('--kind', type=click.Choice(['fp', 'oo']), default='fp')
@click.option('--cmd', multiple=True, type=str)
def do(kind, cmd):
    machinery = globals()[kind]
    cmds = [json.loads(c) for c in cmd]
    print(machinery.__doc__)

    pipes = [cmds] if cmds else PIPES.values()
    for p in pipes:
        f, r = machinery(p)
        print(f, '->', r)

if __name__ == '__main__':
    # $ diff -y <(python pipes.py --kind oo) <(python pipes.py --kind fp)
    do()
