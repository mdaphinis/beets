#!/usr/bin/env python

# This file is part of beets.
# Copyright 2016, Adrian Sampson.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.


import os
import re
import sys
import unittest

pkgpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) or '..'
sys.path.insert(0, pkgpath)


def suite():
    s = unittest.TestSuite()
    # Get the suite() of every module in this directory beginning with
    # "test_".
    for fname in os.listdir(os.path.join(pkgpath, 'test')):
        match = re.match(r'(test_\S+)\.py$', fname)
        if match:
            modname = match.group(1)
            s.addTest(__import__(modname).suite())
    return s


if __name__ == '__main__':
    unittest.main(defaultTest='suite')

