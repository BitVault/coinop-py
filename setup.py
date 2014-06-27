from setuptools import setup, find_packages

setup(name='coinop',
      version='0.0.1',
      description='Crypto-currency conveniences',
      url='http://github.com/BitVault/coinop-py',
      author='Matthew King',
      author_email='matthew@bitvault.io',
      license='MIT',
      packages=find_packages(exclude=[
          u'*.tests', u'*.tests.*', u'tests.*', u'tests']),
      # PyNaCl not listed as a dependency to ensure you install it
      # manually.
      install_requires=[
          'cffi',
          'pytest',
          'pycrypto',
          'python-bitcoinlib',
          'pycoin',
          'PyYAML',
          'ecdsa'
      ],
      zip_safe=False)
