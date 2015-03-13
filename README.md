coinop-py: python crypto currency conveniences


coinop-py is in active development. Bug reports and
pull requests welcome.


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

(if you're not using a virtual environment, you obviously need to run pip
with sudo)

1. Install coinop from PyPI:

    $ pip install coinop
