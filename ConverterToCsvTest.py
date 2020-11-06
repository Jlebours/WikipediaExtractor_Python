import filecmp
import os
import unittest

import ExtractHTML


class MyTestCase(unittest.TestCase):
    def test_sameFiles(self):
        f1 = "output/Comparison_(grammar)-1.csv"
        f2 = "output/Comparison_(grammar)-2.csv"
        self.assertEqual(False, filecmp.cmp(f1, f2))

    def test_internet(self):
        self.assertEqual(0,os.system('ping www.google.com >> log_ping'))

    def testAlgo(self):
        allUrls = ExtractHTML.read_urls()




