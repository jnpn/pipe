from prelude import mapc
from fp import pipe, com

# FONADIC
# BUG: fails with pipe of length one


class Beg:

    def __init__(self, ):
        self.cmds = []

    def __neg__(self, ):
        self.cmds = []
        return self

    def __or__(self, cmd):
        # if cmd is None or cmd is self:
        #     return com(pipe(self.cmds))
        if type(cmd) is End:
            return cmd._(self.cmds)
        else:
            self.cmds.append(cmd)
            return self

    def __repr__(self, ):
        return mapc(str, self.cmds, ' | ')


class End:
    def _(self, cmds):
        return com(pipe(cmds))
