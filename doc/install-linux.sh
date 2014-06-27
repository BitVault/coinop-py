#!/bin/sh
#
#
# See the README before running. Running the commands one at a time by hand so
# you know what you're doing to your box is highly recommended.
#
# These commands should work on at least Ubuntu 13.10 and 14.04, and may need
# tweaking otherwise. libpython-all-dev does not exist in Ubuntu 12.04.


set -x

APT=/usr/bin/apt-get


# Install a build environment for C extensions
$APT install gcc make libpython-all-dev libffi-dev pip

# Insttall PyNaCl manually, as on some systems it will not install properly
# as a dependency:
pip install PyNaCl

# Install the rest normally
python setup.py install
