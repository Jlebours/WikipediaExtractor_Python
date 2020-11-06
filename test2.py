import filecmp
import os
import unittest

import ExtractHTML
import HTMLtoCSV


class MyTestCase(unittest.TestCase):

    def test_internet(self):
        self.assertEqual(0,os.system('ping www.google.com >> log_ping'))

    def test_AllUrls(self):
        allUrls = ExtractHTML.read_urls() # 336 url
        compteur = 0
        for url,name in allUrls :
            compteur = compteur+1
        self.assertEqual(compteur, len(allUrls))


    def test_Algo(self):
        print("Reading url file...")
        # Two dimensional tab with urls and it's name for each one
        allUrls = ExtractHTML.read_urls()
        print(f"You will extract tables from {len(allUrls)} urls")
        print("Starting extraction...")
        for url, name in allUrls:
            tables = ExtractHTML.get_tables(url)
            HTMLtoCSV.convert_csv(tables, name)
        print("End of extraction, you can check the output directory :)")
        #nombre de wikitable qu'il y a dans tous les url
        length = 1000
        DIR = 'output'
        lengthOutput = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
        self.assertEqual(length,lengthOutput)


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






