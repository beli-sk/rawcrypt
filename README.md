Raw encryption tools
====================

A set of command line tools for performing raw encryption written in Python
and using PyCrypto module.

Usage
-----

* ```enc_aes.py <hex_key>``` Encrypt data from stdin using AES algorithm with key given on command line
  in hexadecimal form.
  Output binary encrypted data to stdout.
  Key length can be 16, 24 or 32 bytes.
  Encryption mode is CFB, with IV prepended as first 16-byte block of output.

* ```dec_aes.py <hex_key>``` The oposite - reads encrypted and writes decrypted data.
  Key length can be 16, 24 or 32 bytes.
  IV should be prepended as first 16-byte block of input.

* ```hash_sha256.py``` Reads data from stdin and outputs hexadecimal encoded SHA256 hash on stdout.

License
-------

This software is licensed under the terms of the MIT (expat) license.

    Copyright (C) 2014 Michal Belica
    
    Permission is hereby granted, free of charge, to any person obtaining
    a copy of this software and associated documentation files
    (the "Software"), to deal in the Software without restriction, including
    without limitation the rights to use, copy, modify, merge, publish,
    distribute, sublicense, and/or sell copies of the Software, and to permit
    persons to whom the Software is furnished to do so, subject to
    the following conditions:
    
    The above copyright notice and this permission notice shall be
    included in all copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
    OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
    THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
    DEALINGS IN THE SOFTWARE.
