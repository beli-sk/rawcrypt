#!/usr/bin/python

"""AES Decrypt

Written in 2013 by Michal Belica <devel@beli.sk>
Given away as public domain.

use: dec_aes.py <hex_key>

Decrypt binary from stdin using AES algorithm with key given on command line
in hexadecimal form.
Output decrypted data to stdout.
Key length can be 16, 24 or 32 bytes.
Encryption mode is CFB, IV should be prepended as first 16-byte block of input.
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
if len(k) not in (16, 24, 32):
    raise Exception('Key should be 16, 24 or 32 bit long hex encoded binary data.')

iv = sys.stdin.read(16)
if len(iv) != 16:
    raise Exception('Unable to read 16 bytes of IV.')

dciph = AES.new(k, AES.MODE_CFB, iv)

for block in read_blocks(sys.stdin):
    sys.stdout.write(dciph.decrypt(block))

