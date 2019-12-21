import unittest
import sys
import os

# Path to Project Directory
ppd = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
sys.path.append(os.path.join(ppd, 'web_tools'))

import initializer


class TestInitializer(unittest.TestCase):
    def test_get_groups(self):

        self.assertEqual(initializer.get_groups('http://ruz.spbstu.ru/api/v1/ruz')['3844502/80101'], (101, 28116))

        self.assertEqual(initializer.get_groups('http://ruz.spbstu.ru/api/v1/ruz')['з3532705/80001'], (95, 29141))

        self.assertNotEqual(initializer.get_groups('http://ruz.spbstu.ru/api/v1/ruz')['з3532705/80001'], 1)


if __name__ == '__main__':
    unittest.main()
