
0.3.0 / 2015-06-04
==================

  * Minor weaks and enhancements
  * Switched to pbkdf2_ctypes for performance on passphrase stretching
  * Moved all the coinop modules out of the useless `bit` and `crypto` subpackages. From now on, import directly from `coinop`
  * Replaced PassphraseBox's dependency on NaCl SecretBox with a (AES-CBC-256 then HMAC-SHA256)
  * Removed antiquated tests and installed tox config for testing and basic PassphraseBox tests
  * Python 3.3+ compatibility

0.2.0 / 2015-05-27
==================

  *  network agnosticity possible -- many things don't work
  *  upgrade dependencies (pycoin -> 0.52, python-bitcoinlib -> 0.4.0)
  *  removed txt from license file -- it was bugging me
  *  Cleanup and increased default iterations by a factor of ten to match other coinop packages
  *  refactored seed/secret storage

0.1.3 / 2015-03-24
==================

  *  Refactor seed/secret storage
  *  Minor bug fixes and enhancements

0.1.2 / 2015-03-16
==================

  *  Added functionality to generate/instantiate a MultiWallet using entropic seeds instead of wallet_keys

0.1.1 / 2015-03-13
==================

  * Public availability


0.1.0 / 2015-03-13
==================

  * Initial Release
