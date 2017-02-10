# encoding=utf-8
from __future__ import print_function

import base64
import functools
import json
import os
import string
from datetime import datetime
from inspect import getargspec


def gen_random_str(length):
    return base64.b32encode(os.urandom(3 * length))[:length].lower()


def bytes_to_str(b):
    b = b[2:]
    n = 2
    b_a = [b[i:i + n] for i in range(0, len(b), n)]
    return "".join([chr(int(ib, 16)) for ib in b_a])


def print_dict(d, prefix=''):
    """
    :type d: dict
    """
    for k, v in d.items():
        if isinstance(v, dict):
            print('%s%s:' % (prefix, k))
            print_dict(v, prefix + ' ' * 4)
        else:
            print('%s%s = %s' % (prefix, k, v))


def memoize(fn):
    cache = fn.cache = {}

    @functools.wraps(fn)
    def _memoize(*args, **kwargs):
        kwargs.update(dict(zip(getargspec(fn).args, args)))
        key = tuple(kwargs.get(k, None) for k in getargspec(fn).args)
        if key not in cache:
            cache[key] = fn(**kwargs)
        return cache[key]

    return _memoize


def load_json_from(filename):
    with open(filename, 'r') as f:
        return json.load(f)


def dump_to(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


class Template(string.Template):
    delimiter = '^^'


def load_template(filename):
    with open(filename, 'r') as f:
        s = f.read()
        return Template(s).substitute


def wrap_print(array, n, prefix='', sep=' '):
    maxlen = max([len(s) for s in array])
    fmt = '%-' + str(maxlen) + 's' + sep
    print(prefix, end='')
    for i, v in enumerate(array):
        if i % n == 0 and i:
            print('\n%s' % prefix, end='')
        print(fmt % v, end='')


def timestamp_to_iso(t):
    return datetime.fromtimestamp(int(t)).isoformat()
