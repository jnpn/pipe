from subprocess import PIPE, Popen
from functools import reduce
from prelude import mapc

# [Pi]
# [Pi, Pj(Pi)]
# [Pi, Pj(Pi), Pk(Pj)]


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


def show(pipe):
    return mapc(str, map(lambda cmd: ' '.join(cmd), pipe), ' | ')
