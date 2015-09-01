from collections import OrderedDict

PIPES = OrderedDict({
    'es': [
        ['echo', 'foo bar baz'],
        ['sed', 's, , @@@, g']
    ],
    'ps': [
        ['echo', 'foo bar baz'],
        ['sed', 's, , | , g']
    ],
    'wat': [
        ['echo', ' oob rab zab'],
        ['sed', 's, b, b\\n, g'],
        ['sed', 's, \\([^ ]*\\), >>> \\1 !, g']
    ],
    'wut': [
        ['echo', ' oob rab zab'],
        ['sed', 's, b, b\\n, g'],
        ['sed', 's, \\([^ ]*\\), ( \\1 ), g']
    ],
    'lgs': [
        ['ls', '-a', '/home/agumonkey/'],
        ['grep', 'bash'],
        ['sed', 's, bash, BASH, g']
    ],
    'zw': [
        ['zcat', '/home/agumonkey/test.log.tar.gz'],
        ['grep', '-a', '-i', 'bogus'],
        ['wc', '-l']
    ]
})
