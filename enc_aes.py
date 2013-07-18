#!/usr/bin/python

"""AES Encrypt

Written in 2013 by Michal Belica <devel@beli.sk>
Given away as public domain.

use: enc_aes.py <hex_key>

Encrypt data from stdin using AES algorithm with key given on command line
in hexadecimal form.
Output binary encrypted data to stdout.
Key length can be 16, 24 or 32 bytes.
Encryption mode is CFB, with IV prepended as first 16-byte block of output.
"""

import sys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def read_blocks(f, size=1024):
    while True:
        data = f.read(size)
        if not data:
            break
        yield data

k = sys.argv[1].decode('hex')

iv = get_random_bytes(16)
eciph = AES.new(k, AES.MODE_CFB, iv)

sys.stdout.write(iv)

for block in read_blocks(sys.stdin):
    sys.stdout.write(eciph.encrypt(block))

