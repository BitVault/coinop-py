coinop-py: python crypto currency conveniences


coinop-py is still alpha code but is in active development. Bug reports and
patches welcome.


Installing coinop-py:

Ubuntu:

Prerequisites:

1. A python 2.7 environment (your distro probably does this as part of the base
   system, but the nicer way is with pyenv and/or virtualenv). coinop-py is
   currently developed under 2.7.7.

2. A python extension build environment. You probably have most or all of this
   on your machine already, but the following should do it on a bare system:

   $ sudo apt-get install gcc make libpython-all-dev libffi-dev python-pip

Installing:

1. *Manually* install PyNaCl to work around an install bug on some machines:

    $ pip install PyNaCl

(if you're not using a virtual environment, you obviously need to run pip
with sudo)

2. Install coinop from PyPI:

    $ pip install coinop

(if you're not using a virtual environment, you obviously need to run pip
with sudo)
