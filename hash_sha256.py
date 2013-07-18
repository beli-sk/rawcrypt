#!/usr/bin/python

"""SHA256 hash

Written in 2013 by Michal Belica <devel@beli.sk>
Given away as public domain.

Reads data from stdin and outputs hexadecimal encoded SHA256 hash on stdout.
"""

import sys
from Crypto.Hash import SHA256

def read_blocks(f, size=1024):
    while True:
        data = f.read(size)
        if len(data) < size:
            if len(data) > 0:
                yield data
            break
        yield data

h = SHA256.new()
for block in read_blocks(sys.stdin):
    h.update(block)
sys.stdout.write(h.digest().encode('hex')+"\n")

