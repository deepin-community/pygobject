#!/usr/bin/env python3

import unittest
import sys
from gi.repository import GLib


class TestGI(unittest.TestCase):
    def test_glib_enum(self):
        '''GLib enum'''
        self.assertEqual(GLib.IOCondition.IN.value_nicks, ['in'])

    def test_glib_flag(self):
        '''GLib flag'''
        nicks = set(GLib.IOFlags.IS_READABLE.value_nicks)
        # https://gitlab.gnome.org/GNOME/pygobject/-/issues/542
        nicks.discard('none')
        self.assertEqual(nicks, set(['is_readable']))

    def test_method(self):
        '''GLib method call'''

        self.assertIn(GLib.find_program_in_path('bash'), ('/bin/bash', '/usr/bin/bash'))


unittest.main(testRunner=unittest.TextTestRunner(stream=sys.stdout, verbosity=2))
