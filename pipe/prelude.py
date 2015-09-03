'''
Some helper functions.
'''


def mapc(f, l, s=' '):
    '''Mapconcat: map f over l then s.join the result.'''
    return s.join(map(f, l))


def print_decoded(result, codec='utf8'):
    '''To show the pipe results in a less crude way.'''
    print(result.decode(codec))
