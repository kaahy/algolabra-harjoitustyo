import unittest
from ratkaisuohjelma import Ratkaisuohjelma

class TestRatkaisuohjelma(unittest.TestCase):
    def setUp(self):
        pass

    def test_oikea_ratkaisu_1(self):
        # kuuluu onnistua, koska nyt alkuvaiheessa ohjelma antaa aina tämän saman ratkaisun

        aloitustilanne =  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '-', '13', '14', '15']
        ohjelma = Ratkaisuohjelma(aloitustilanne)
        
        oikea_ratkaisu = [13, 14, 15]
        saatu_ratkaisu = ohjelma.ratkaisu()

        self.assertEqual(oikea_ratkaisu, saatu_ratkaisu)

    def test_oikea_ratkaisu_2(self):
        # kuuluu epäonnistua, koska ohjelma ei toimi vielä

        aloitustilanne =  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '-', '14', '15']
        ohjelma = Ratkaisuohjelma(aloitustilanne)
        
        oikea_ratkaisu = [14, 15]
        saatu_ratkaisu = ohjelma.ratkaisu()

        self.assertEqual(oikea_ratkaisu, saatu_ratkaisu)

    def test_oikeat_siirtymavaihtoehdot_kun_tyhja_oikeassa_alanurkassa(self):
        tilanne =  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '-']
        ohjelma = Ratkaisuohjelma(tilanne)

        oikeat_vaihtoehdot = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '-', '15'],
                              ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '-', '13', '14', '15', '12']]

        saadut_vaihtoehdot = ohjelma.naapuritilanteet(tilanne)
        
        self.assertEqual(sorted(oikeat_vaihtoehdot), sorted(saadut_vaihtoehdot))

    def test_oikeat_siirtymavaihtoehdot_kun_tyhja_vasemmassa_ylanurkassa(self):
        tilanne =  ['-', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
        ohjelma = Ratkaisuohjelma(tilanne)

        oikeat_vaihtoehdot = [['1', '-', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'],
                              ['4', '1', '2', '3', '-', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']]

        saadut_vaihtoehdot = ohjelma.naapuritilanteet(tilanne)
        
        self.assertEqual(sorted(oikeat_vaihtoehdot), sorted(saadut_vaihtoehdot))

    def test_oikeat_siirtymavaihtoehdot_kun_tyhja_keskella(self):
        tilanne =  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '10', '11', '12', '13', '14', '15']
        ohjelma = Ratkaisuohjelma(tilanne)

        oikeat_vaihtoehdot = [['1', '2', '3', '4', '5', '6', '7', '8', '-', '9', '10', '11', '12', '13', '14', '15'],
                              ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '-', '11', '12', '13', '14', '15'],
                              ['1', '2', '3', '4', '5', '-', '7', '8', '9', '6', '10', '11', '12', '13', '14', '15'],
                              ['1', '2', '3', '4', '5', '6', '7', '8', '9', '13', '10', '11', '12', '-', '14', '15']]

        saadut_vaihtoehdot = ohjelma.naapuritilanteet(tilanne)
        
        self.assertEqual(sorted(oikeat_vaihtoehdot), sorted(saadut_vaihtoehdot))

    def test_oikeat_siirtymavaihtoehdot_kun_tyhja_ylarivin_keskella(self):
        tilanne =  ['1', '2', '-', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '3']
        ohjelma = Ratkaisuohjelma(tilanne)

        oikeat_vaihtoehdot = [['1', '-', '2', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '3'],
                              ['1', '2', '4', '-', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '3'],
                              ['1', '2', '7', '4', '5', '6', '-', '8', '9', '10', '11', '12', '13', '14', '15', '3']]

        saadut_vaihtoehdot = ohjelma.naapuritilanteet(tilanne)
        
        self.assertEqual(sorted(oikeat_vaihtoehdot), sorted(saadut_vaihtoehdot))

    def test_oikeat_siirtymavaihtoehdot_kun_tyhja_alarivin_keskella(self):
        tilanne =  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '-', '15', '14']
        ohjelma = Ratkaisuohjelma(tilanne)

        oikeat_vaihtoehdot = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '-', '13', '15', '14'],
                              ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '-', '14'],
                              ['1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '11', '12', '13', '10', '15', '14']]

        saadut_vaihtoehdot = ohjelma.naapuritilanteet(tilanne)
        
        self.assertEqual(sorted(oikeat_vaihtoehdot), sorted(saadut_vaihtoehdot))

    def test_oikeat_siirtymavaihtoehdot_kun_tyhja_vasemman_sarakkeen_keskella(self):
        tilanne =  ['1', '2', '3', '4', '5', '6', '7', '8', '-', '10', '11', '12', '13', '14', '15', '9']
        ohjelma = Ratkaisuohjelma(tilanne)

        oikeat_vaihtoehdot = [['1', '2', '3', '4', '-', '6', '7', '8', '5', '10', '11', '12', '13', '14', '15', '9'],
                              ['1', '2', '3', '4', '5', '6', '7', '8', '10', '-', '11', '12', '13', '14', '15', '9'],
                              ['1', '2', '3', '4', '5', '6', '7', '8', '13', '10', '11', '12', '-', '14', '15', '9']]

        saadut_vaihtoehdot = ohjelma.naapuritilanteet(tilanne)
        
        self.assertEqual(sorted(oikeat_vaihtoehdot), sorted(saadut_vaihtoehdot))

    def test_oikeat_siirtymavaihtoehdot_kun_tyhja_oikean_sarakkeen_keskella(self):
        tilanne =  ['1', '2', '3', '4', '5', '6', '7', '-', '9', '10', '11', '12', '13', '14', '15', '8']
        ohjelma = Ratkaisuohjelma(tilanne)

        oikeat_vaihtoehdot = [['1', '2', '3', '4', '5', '6', '-', '7', '9', '10', '11', '12', '13', '14', '15', '8'],
                              ['1', '2', '3', '-', '5', '6', '7', '4', '9', '10', '11', '12', '13', '14', '15', '8'],
                              ['1', '2', '3', '4', '5', '6', '7', '12', '9', '10', '11', '-', '13', '14', '15', '8']]

        saadut_vaihtoehdot = ohjelma.naapuritilanteet(tilanne)
        
        self.assertEqual(sorted(oikeat_vaihtoehdot), sorted(saadut_vaihtoehdot))

    def test_inversioiden_maara(self):
        tilanne =  ['3', '15', '1', '-', '12', '11', '6', '9', '4', '14', '7', '13', '10', '2', '8', '5']
        ohjelma = Ratkaisuohjelma(tilanne)

        inversioita = 57

        self.assertEqual(inversioita, ohjelma.laske_inversiot(tilanne))

    def test_kertoo_että_ratkaistavissa1(self):
        tilanne =  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '-']
        ohjelma = Ratkaisuohjelma(tilanne)
        
        self.assertEqual(True, ohjelma.onko_ratkaistavissa(tilanne))

    def test_kertoo_että_ratkaistavissa2(self):
        tilanne =  ['3', '15', '1', '-', '12', '11', '6', '9', '4', '14', '7', '13', '10', '2', '8', '5'] # oikean nettipelin yksi aloitustilanne
        ohjelma = Ratkaisuohjelma(tilanne)
        
        self.assertEqual(True, ohjelma.onko_ratkaistavissa(tilanne))

    def test_kertoo_että_ei_ratkaistavissa1(self):
        tilanne =  ['-', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
        ohjelma = Ratkaisuohjelma(tilanne)
        
        self.assertEqual(False, ohjelma.onko_ratkaistavissa(tilanne))

    def test_kertoo_että_ei_ratkaistavissa2(self):
        tilanne =  ['13', '9', '5', '1', '14', '10', '6', '2', '15', '11', '7', '3', '-', '12', '8', '4'] # Wikipediasta 15-peli-artikkelista
        ohjelma = Ratkaisuohjelma(tilanne)
        
        self.assertEqual(False, ohjelma.onko_ratkaistavissa(tilanne))
