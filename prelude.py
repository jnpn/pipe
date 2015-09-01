def mapc(f, l, s=' '):
    '''Mapconcat: map f over l then s.join the result.'''
    return s.join(map(f, l))
