#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

class HelloWorldTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_say_hello(self):
        out_string = "hello"
        self.assertEqual(out_string, "hello")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()