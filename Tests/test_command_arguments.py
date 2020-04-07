# https://docs.python.org/3.3/library/argparse.html

import unittest
import sys
import argparse

class TestClass (unittest.TestCase):
    command_line_input = input
    def test_no_args_given(self):
        sys.argv = ['thecastleargv', '--foo']
        parser = argparse.ArgumentParser()
        parser.add_argument('--foo', action='store_true')
        args = parser.parse_args()

        self.assertTrue('foo' in args)
        self.assertFalse('bar' in args)
        self.assertTrue(args.foo)

    def test_empty_list(self):
        sys.argv = ["thecastleargv"]
        parser = argparse.ArgumentParser()
        parser.add_argument('--foo', action='append', default=[])
        args = parser.parse_args()
        self.assertEqual(args.foo, [])