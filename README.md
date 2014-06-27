coinop-py: python crypto currency conveniences


coinop-py is still alpha code but is in active development. Bug reports and
patches welcome.


Installing coinop-py:

Linux:

1. Install a python 2.7 environment (your distro probably does this as part of
   the base system, but the nicer way is with pyenv and virtualenv).  It is
   developed under 2.7.7, and while it may work with earlier versions that is
   currently untested. The longer-term goal is compatibility with at least the
   2.7 and perhaps the 2.6 series. If those versions don't fit your needs drop
   us a line and we can talk about it.

2. Clone the git repository:

    $ git clone https://github.com/BitVault/coinop-py.git
    $ cd coinop-py

2. If you like to live dangerously, you can simply run

    $ sudo ./doc/install-linux.sh

from the root directory (no sudo needed if you're using a tool like pyenv).
Otherwise, read the script and run the relevant commands yourself when you're
convinced they'll do no harm.
