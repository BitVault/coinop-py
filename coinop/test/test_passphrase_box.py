from __future__ import unicode_literals

import pytest
from random import randint
from os import urandom
from ..passphrasebox import PassphraseBox

@pytest.fixture(scope="session")
def passphrase():
    return 'asdfasdf'

@pytest.fixture
def plaintext():
    return 'hellohellohello!'

@pytest.fixture
def encrypted():
    return {'ciphertext': 'e64cd877f968c408f9a0a2dbcf8e14667ef825c4349e1822ac4896a2553a751ec2346a8321027a3f947243c011025163',
            'salt': '2eb78d2e7331e8462847a00f325d94b5',
            'iterations': 97917,
            'iv': '1bc9947601b4292059d4da59852dba30'}

@pytest.fixture
def salt(encrypted):
    return encrypted['salt']

@pytest.fixture
def iv(encrypted):
    return encrypted['iv']

@pytest.fixture
def iterations(encrypted):
    return encrypted['iterations']


class TestPassphraseBox(object):
    def test_init(self, passphrase, salt, iterations):
        pass

    def test_encrypt(self, passphrase, plaintext):
        pass

    def test_decrypt(self, passphrase, encrypted):
        pass

    def test__encrypt(self, passphrase, iv):
        pass

    def test__decrypt(self, passphrase, iv):
        pass

    def test_associativity(self, passphrase, plaintext):
        enc = PassphraseBox.encrypt(passphrase, plaintext)
        dec = PassphraseBox.decrypt(passphrase, enc)
        assert plaintext == dec
