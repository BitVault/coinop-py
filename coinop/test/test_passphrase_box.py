from __future__ import unicode_literals

import pytest
from random import randint
from os import urandom
from ..passphrasebox import PassphraseBox

testdata = [('asdfasdf','hellohellohello!',
             {'ciphertext': 'e64cd877f968c408f9a0a2dbcf8e14667ef825c4349e1822ac4896a2553a751ec2346a8321027a3f947243c011025163',
              'salt': '2eb78d2e7331e8462847a00f325d94b5',
              'iterations': 97917,
              'iv': '1bc9947601b4292059d4da59852dba30'}),
            ('asdfasdf','',
             {'ciphertext': '5d2e1737fe8fd34b75af7d0163367f9db9e55a10fac0639bef5d476a140ff4ee',
              'salt': 'c753748ca6c1be684432548d9c8c76b0',
              'iterations': 107569,
              'iv': '4b362819ab6f0d0040e43eaab5802e0f'}),
            ('','',
             {'ciphertext': '1b541bdd86bbdcb72e845cae4653426422222080d407f81025a01cd8dddb9ee0',
              'iterations': 108498,
              'iv': '082b79b964a65a1d0ad68532a3b5016d',
              'salt': 'f5d38842be5b320e41b71041632b2b27'})]

def pytest_generate_tests(metafunc):
    metafunc.parametrize('passphrase, plaintext, encrypted', testdata)

class TestPassphraseBox(object):

    def test_associativity(self, passphrase, plaintext, encrypted):
        enc = PassphraseBox.encrypt(passphrase, plaintext)
        dec = PassphraseBox.decrypt(passphrase, enc)
        stored_dec = PassphraseBox.decrypt(passphrase, encrypted)
        assert plaintext == dec == stored_dec

    def test_decrypt(self, passphrase, plaintext, encrypted):
        assert PassphraseBox.decrypt(passphrase, encrypted) == plaintext

    def test__encrypt(self, passphrase, plaintext, encrypted):
        assert encrypted == PassphraseBox(
            passphrase,
            salt=encrypted['salt'],
            iterations=encrypted['iterations'])._encrypt(plaintext,
                                                         encrypted['iv'])

    def test__decrypt(self, passphrase, plaintext, encrypted):
        assert plaintext == PassphraseBox(
            passphrase,
            salt=encrypted['salt'],
            iterations=encrypted['iterations'])._decrypt(encrypted['ciphertext'],
                                                         encrypted['iv'])
