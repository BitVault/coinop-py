from __future__ import unicode_literals

import pytest
from random import randint
from os import urandom
from coinop.passphrasebox import PassphraseBox

@pytest.fixture(scope="session")
def passphrase():
    return 'asdf'

@pytest.fixture
def plaintext():
    return 'hellohellohello!'

@pytest.fixture
def encrypted():
    return {'ciphertext': 'd9c92b01601524ce6d1a0a0f520107455ba349c82e507fc1e7a2233a02f59011099b3f68b105c8eb311b61b2a4be7db4',
            'salt': 'c20ce26af711de80c105492f5eee4b78',
            'iterations': 94077,
            'iv': '9139a0afc042874ffffd6a751cd41c6c'}

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
