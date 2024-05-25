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

    def test_oikeat_valivaiheet_1(self):
        # kuuluu onnistua, koska nyt alkuvaiheessa ohjelma antaa aina nämä samat välivaiheet

        aloitustilanne =  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '-', '13', '14', '15']
        ohjelma = Ratkaisuohjelma(aloitustilanne)
        
        oikeat_valivaiheet = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '-', '13', '14', '15'],
                              ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '-', '14', '15'],
                              ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '-', '15'],
                              ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '-']]

        saadut_valivaiheet = ohjelma.valivaiheet()

        self.assertEqual(oikeat_valivaiheet, saadut_valivaiheet)

    def test_oikeat_valivaiheet_2(self):
        # kuuluu epäonnistua, koska ohjelma ei toimi vielä

        aloitustilanne =  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '-', '14', '15']
        ohjelma = Ratkaisuohjelma(aloitustilanne)
        
        oikeat_valivaiheet = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '-', '14', '15'],
                              ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '-', '15'],
                              ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '-']]

        saadut_valivaiheet = ohjelma.valivaiheet()

        self.assertEqual(oikeat_valivaiheet, saadut_valivaiheet)
