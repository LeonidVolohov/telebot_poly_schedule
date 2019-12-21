import unittest
import sys
import os

# Path to Project Directory
ppd = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
sys.path.append(os.path.join(ppd, 'utils'))

import group_funcs


class TestGroupFuncs(unittest.TestCase):

    def test_parse_group_from_user(self):

        with self.assertRaises(SyntaxError):
            group_funcs.parse_group_from_user('')

        with self.assertRaises(SyntaxError):
            group_funcs.parse_group_from_user('/set_group')
            print()

        with self.assertRaises(SyntaxError):
            group_funcs.parse_group_from_user('/set_group 3530904/70101 abc')

        with self.assertRaises(ValueError):
            group_funcs.parse_group_from_user('/set_group 3530904/70101')

    def test_remember_relation(self):
        pass


if __name__ == '__main__':
    unittest.main()
