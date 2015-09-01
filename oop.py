from fp import pipe, com, show


# FONADIC
# BUG: fails with pipe of length one


class Beg:

    def __init__(self, cmds=[]):
        self.cmds = cmds[:]

    def __or__(self, cmd):
        '''
        Beg(cmds) | [cmd, args...]
              |
              `- Beg(cmds + [cmd]) | ... .

        Cons like list construction with
        context and termination.
        '''
        if type(cmd) is End:
            return cmd._(self.cmds)
        else:
            return Beg(self.cmds + [cmd])

    def __repr__(self, ):
        return show(self.cmds)


class End:
    def _(self, cmds):
        return com(pipe(cmds))


# Tests


def t0():
    return Beg() | ["ls", "/tmp"] | ["wc"] | End()
