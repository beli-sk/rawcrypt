Raw encryption tools
====================

A set of command line tools for performing raw encryption written in Python
and using PyCrypto module.

This project has been made obsolete by [Rawcrypt 2](https://github.com/beli-sk/rawcrypt2).


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


Known issues
------------

* data is not authenticated

* key given on command line


License
-------

Written by Michal Belica <https://beli.sk> in 2013 and 2014.

Licenced under [CC0](https://creativecommons.org/publicdomain/zero/1.0/).

To the extent possible under law, the author has waived all copyright
and related or neighboring rights to Rawcrypt.

