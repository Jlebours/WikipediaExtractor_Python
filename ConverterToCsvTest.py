import filecmp
import unittest


class MyTestCase(unittest.TestCase):
    def test_sameFiles(self):
        f1 = "output/Comparison_(grammar)-1.csv"
        f2 = "output/Comparison_(grammar)-2.csv"
        self.assertFalse(filecmp.cmp(f1, f2))


    def test_VeriteTerrain1(self):
        f1 = "output/Comparison_between_Esperanto_and_Ido-1.csv"
        f2 = "verite/Comparison_between_Esperanto_and_Ido-1 test.csv"
        self.assertFalse(filecmp.cmp(f1, f2))

    def test_VeriteTerrain2(self):
        f1 = "output/Comparison_between_Ido_and_Interlingua-1.csv"
        f2 = "verite/Comparison_between_Ido_and_Interlingua-1 test.csv"
        self.assertTrue(filecmp.cmp(f1, f2))