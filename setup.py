from setuptools import setup, find_packages


setup(name='coinop',
      version='0.1.0',
      description='Crypto-currency conveniences',
      url='http://github.com/BitVault/coinop-py',
      author='Matthew King',
      author_email='matthew@bitvault.io',
      license='MIT',
      packages=find_packages(exclude=[
          u'*.tests', u'*.tests.*', u'tests.*', u'tests']),
      install_requires=[
          # Not listed explicitly to ensure you install PyNaCl by hand--
          # see README
          #'PyNaCl',
          'cffi',
          'pytest',
          'pycrypto',
          'python-bitcoinlib',
          'pycoin',
          'PyYAML',
          'ecdsa'
      ],
      zip_safe=False)
