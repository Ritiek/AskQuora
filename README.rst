AskQuora
========

|pypi.python.org| |build Status|

Quora Q&A right from the command line!

Inspired by https://github.com/gleitz/howdoi

Installation & Usage:
---------------------

::

    sudo pip install -U askquora

or if you like to live on the bleeding edge:

::

    sudo python setup.py install

Run it using ``askquora``

::

    usage: askquora [-h] [-n] [QUERY [QUERY ...]]

    Quora Q&A right from the command-line

    positional arguments:
      QUERY           the question to find the answer of

    optional arguments:
      -h, --help      show this help message and exit
      -n, --no-color  do not colorize or style text

Contributing:
-------------

Any PR's in bug fixes, features or even this documentation are most
welcome!

Disclaimer:
-----------

This is not an official Quora product.

License:
--------

``The MIT License``

.. |pypi.python.org| image:: https://img.shields.io/pypi/v/AskQuora.svg
   :target: https://pypi.org/project/AskQuora/
.. |build Status| image:: https://travis-ci.org/ritiek/AskQuora.svg?branch=master
   :target: https://travis-ci.org/ritiek/AskQuora/
