import filecmp
import os
import unittest

import ExtractHTML
import HTMLtoCSV

'''
Before running tests don't forget to run the program ! :) 
'''

class MyTestCase(unittest.TestCase):
    '''
    Test on internet Connection
    '''

    def test_internet(self):
        self.assertEqual(0, os.system('ping www.google.com >> log_ping'))

    '''
    Test to check if all URLS are all taken
    '''

    def test_AllUrls(self):
        allUrls = ExtractHTML.read_urls()
        compteur = 0
        for url, name in allUrls:
            compteur = compteur + 1
        self.assertEqual(compteur, len(allUrls))

        # self.assertEqual(result, allUrls)

    '''
    Test in comment cause it was not working due to the main that we have to launch in konsole

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
        length = 1685
        DIR = 'output'
        lengthOutput = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
        self.assertEqual(length,lengthOutput)
'''
    '''
    Test to compare two files
    '''

    def test_sameFiles(self):
        f1 = "output/Comparison_(grammar)_1.csv"
        f2 = "output/Comparison_(grammar)_2.csv"
        self.assertFalse(filecmp.cmp(f1, f2))

    '''
    Test to compare two identical files
    '''

    def test_VeriteTerrain1(self):
        f1 = "output/Comparison_(grammar)_1.csv"
        f2 = "verite/VeriteTerrainComparison_(grammar)_1.csv"
        self.assertTrue(filecmp.cmp(f1, f2))

    '''
    Test to compare two differents files
    '''

    def test_VeriteTerrain2(self):
        f1 = "output/Comparison_(grammar)_2.csv"
        f2 = "verite/VeriteTerrainComparison_(grammar)_1.csv"
        self.assertFalse(filecmp.cmp(f1, f2))

    '''
    Test to compare that all csv files are differents 
    '''

    def test_differentFiles(self):
        listOfAlreadycheck = []
        count = 0
        files = os.listdir("output")
        same = False
        listeString = []
        for name in files:
            for names in files:
                if not (name == names):
                    if (filecmp.cmp("output/" + name, "output/" + names)):
                        for alreadyCheck in listOfAlreadycheck :
                            if not((alreadyCheck == [name,names]) or (alreadyCheck == [names, name])):
                                listOfAlreadycheck.append([name,names])
                                count = count+1
                                same = True


        self.assertFalse(same)
        print("the number of same files in all the output directory is :")
        print(count)

