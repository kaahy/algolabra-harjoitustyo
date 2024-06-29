import unittest
from ratkaisuohjelma import Ratkaisuohjelma

class TestRatkaisuohjelma(unittest.TestCase):
    def setUp(self):
        pass

    def test_oikeat_siirtymavaihtoehdot_kun_tyhja_oikeassa_alanurkassa(self):
        tilanne =  ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '-')
        ohjelma = Ratkaisuohjelma(tilanne)

        oikeat_vaihtoehdot = [('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '-', '15'),
                              ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '-', '13', '14', '15', '12')]

        saadut_vaihtoehdot = [x[1] for x in ohjelma.naapuritilanteet(tilanne)]

        self.assertEqual(sorted(oikeat_vaihtoehdot), sorted(saadut_vaihtoehdot))

    def test_oikeat_siirtymavaihtoehdot_kun_tyhja_vasemmassa_ylanurkassa(self):
        tilanne =  ('-', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15')
        ohjelma = Ratkaisuohjelma(tilanne)

        oikeat_vaihtoehdot = [('1', '-', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'),
                              ('4', '1', '2', '3', '-', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15')]

        saadut_vaihtoehdot = [x[1] for x in ohjelma.naapuritilanteet(tilanne)]

        self.assertEqual(sorted(oikeat_vaihtoehdot), sorted(saadut_vaihtoehdot))

    def test_oikeat_siirtymavaihtoehdot_kun_tyhja_keskella(self):
        tilanne = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '10', '11', '12', '13', '14', '15')
        ohjelma = Ratkaisuohjelma(tilanne)

        oikeat_vaihtoehdot = [('1', '2', '3', '4', '5', '6', '7', '8', '-', '9', '10', '11', '12', '13', '14', '15'),
                              ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '-', '11', '12', '13', '14', '15'),
                              ('1', '2', '3', '4', '5', '-', '7', '8', '9', '6', '10', '11', '12', '13', '14', '15'),
                              ('1', '2', '3', '4', '5', '6', '7', '8', '9', '13', '10', '11', '12', '-', '14', '15')]

        saadut_vaihtoehdot = [x[1] for x in ohjelma.naapuritilanteet(tilanne)]

        self.assertEqual(sorted(oikeat_vaihtoehdot), sorted(saadut_vaihtoehdot))

    def test_oikeat_siirtymavaihtoehdot_kun_tyhja_ylarivin_keskella(self):
        tilanne =  ('1', '2', '-', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '3')
        ohjelma = Ratkaisuohjelma(tilanne)

        oikeat_vaihtoehdot = [('1', '-', '2', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '3'),
                              ('1', '2', '4', '-', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '3'),
                              ('1', '2', '7', '4', '5', '6', '-', '8', '9', '10', '11', '12', '13', '14', '15', '3')]

        saadut_vaihtoehdot = [x[1] for x in ohjelma.naapuritilanteet(tilanne)]

        self.assertEqual(sorted(oikeat_vaihtoehdot), sorted(saadut_vaihtoehdot))

    def test_oikeat_siirtymavaihtoehdot_kun_tyhja_alarivin_keskella(self):
        tilanne =  ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '-', '15', '14')
        ohjelma = Ratkaisuohjelma(tilanne)

        oikeat_vaihtoehdot = [('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '-', '13', '15', '14'),
                              ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '-', '14'),
                              ('1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '11', '12', '13', '10', '15', '14')]

        saadut_vaihtoehdot = [x[1] for x in ohjelma.naapuritilanteet(tilanne)]

        self.assertEqual(sorted(oikeat_vaihtoehdot), sorted(saadut_vaihtoehdot))

    def test_oikeat_siirtymavaihtoehdot_kun_tyhja_vasemman_sarakkeen_keskella(self):
        tilanne =  ('1', '2', '3', '4', '5', '6', '7', '8', '-', '10', '11', '12', '13', '14', '15', '9')
        ohjelma = Ratkaisuohjelma(tilanne)

        oikeat_vaihtoehdot = [('1', '2', '3', '4', '-', '6', '7', '8', '5', '10', '11', '12', '13', '14', '15', '9'),
                              ('1', '2', '3', '4', '5', '6', '7', '8', '10', '-', '11', '12', '13', '14', '15', '9'),
                              ('1', '2', '3', '4', '5', '6', '7', '8', '13', '10', '11', '12', '-', '14', '15', '9')]

        saadut_vaihtoehdot = [x[1] for x in ohjelma.naapuritilanteet(tilanne)]

        self.assertEqual(sorted(oikeat_vaihtoehdot), sorted(saadut_vaihtoehdot))

    def test_oikeat_siirtymavaihtoehdot_kun_tyhja_oikean_sarakkeen_keskella(self):
        tilanne =  ('1', '2', '3', '4', '5', '6', '7', '-', '9', '10', '11', '12', '13', '14', '15', '8')
        ohjelma = Ratkaisuohjelma(tilanne)

        oikeat_vaihtoehdot = [('1', '2', '3', '4', '5', '6', '-', '7', '9', '10', '11', '12', '13', '14', '15', '8'),
                              ('1', '2', '3', '-', '5', '6', '7', '4', '9', '10', '11', '12', '13', '14', '15', '8'),
                              ('1', '2', '3', '4', '5', '6', '7', '12', '9', '10', '11', '-', '13', '14', '15', '8')]

        saadut_vaihtoehdot = [x[1] for x in ohjelma.naapuritilanteet(tilanne)]

        self.assertEqual(sorted(oikeat_vaihtoehdot), sorted(saadut_vaihtoehdot))

    def test_inversioiden_maara(self):
        tilanne =  ('3', '15', '1', '-', '12', '11', '6', '9', '4', '14', '7', '13', '10', '2', '8', '5')
        ohjelma = Ratkaisuohjelma(tilanne)

        inversioita = 57

        self.assertEqual(inversioita, ohjelma.laske_inversiot(tilanne))

    def test_kertoo_että_ratkaistavissa_1(self):
        tilanne =  ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '-')
        ohjelma = Ratkaisuohjelma(tilanne)

        self.assertEqual(True, ohjelma.onko_ratkaistavissa(tilanne))

    def test_kertoo_että_ratkaistavissa_2(self):
        tilanne =  ('3', '15', '1', '-', '12', '11', '6', '9', '4', '14', '7', '13', '10', '2', '8', '5') # oikean nettipelin yksi aloitustilanne
        ohjelma = Ratkaisuohjelma(tilanne)

        self.assertEqual(True, ohjelma.onko_ratkaistavissa(tilanne))

    def test_kertoo_että_ei_ratkaistavissa_1(self):
        tilanne =  ('-', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15')
        ohjelma = Ratkaisuohjelma(tilanne)

        self.assertEqual(False, ohjelma.onko_ratkaistavissa(tilanne))

    def test_kertoo_että_ei_ratkaistavissa_2(self):
        tilanne =  ('13', '9', '5', '1', '14', '10', '6', '2', '15', '11', '7', '3', '-', '12', '8', '4') # Wikipediasta 15-peli-artikkelista
        ohjelma = Ratkaisuohjelma(tilanne)

        self.assertEqual(False, ohjelma.onko_ratkaistavissa(tilanne))

    def test_ratkaisu_on_None_jos_ei_ratkaistavissa(self):
        aloitustilanne =  ('13', '9', '5', '1', '14', '10', '6', '2', '15', '11', '7', '3', '-', '12', '8', '4')
        ohjelma = Ratkaisuohjelma(aloitustilanne)

        self.assertEqual(None, ohjelma.ratkaisu())

    def test_ratkaisu_on_tyhja_lista_jos_aloitustilanne_on_ratkaisu(self):
        aloitustilanne =  ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '-')
        ohjelma = Ratkaisuohjelma(aloitustilanne)

        self.assertEqual([], ohjelma.ratkaisu())

    def test_lyhyin_ratkaisun_pituus(self):
        tilanne =  ('-', '1', '2', '3', '5', '6', '7', '4', '9', '10', '11', '8', '13', '14', '15', '12')
        # tyhjä siirtyy vasemmasta ylänurkasta esim. ensin oikeaan ylänurkkaan (3 siirtoa) ja siitä oikeaan alanurkkaan (toiset 3 siirtoa)

        ohjelma = Ratkaisuohjelma(tilanne)

        self.assertEqual(6, len(ohjelma.ratkaisu()))

    def test_manhattan_distance_1(self):
        tilanne =  ('-', '1', '2', '3', '5', '6', '7', '4', '9', '10', '11', '8', '13', '14', '15', '12')
        ohjelma = Ratkaisuohjelma(tilanne)

        self.assertEqual(6, ohjelma.manhattan_distance(tilanne))

    def test_manhattan_distance_2(self):
        tilanne =  ('1', '2', '3', '4', '5', '6', '12', '7', '9', '10', '11', '8', '13', '14', '-', '15')
        #            -    -    -    -    -    -     2    1    -    -     -     1     -     -    -     1

        ohjelma = Ratkaisuohjelma(tilanne)

        self.assertEqual(5, ohjelma.manhattan_distance(tilanne))

    def test_oikeat_valivaiheet_1(self):
        aloitustilanne = ('-', '2', '3', '4', '1', '6', '7', '8', '5', '9', '10', '12', '13', '14', '11', '15')
        ohjelma = Ratkaisuohjelma(aloitustilanne)
        ohjelma.ratkaisu()

        oikeat_valivaiheet = [('-', '2', '3', '4', '1', '6', '7', '8', '5', '9', '10', '12', '13', '14', '11', '15'),
                              ('1', '2', '3', '4', '-', '6', '7', '8', '5', '9', '10', '12', '13', '14', '11', '15'),
                              ('1', '2', '3', '4', '5', '6', '7', '8', '-', '9', '10', '12', '13', '14', '11', '15'),
                              ('1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '10', '12', '13', '14', '11', '15'),
                              ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '-', '12', '13', '14', '11', '15'),
                              ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '-', '15'),
                              ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '-')]

        self.assertEqual(oikeat_valivaiheet, ohjelma.valivaiheet())

    def test_oikeat_valivaiheet_2(self):
        aloitustilanne = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '15', '-', '13', '14', '12', '11')
        ohjelma = Ratkaisuohjelma(aloitustilanne)
        ohjelma.ratkaisu()

        oikeat_valivaiheet = [('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '15', '-', '13', '14', '12', '11'),
                              ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '15', '11', '13', '14', '12', '-'),
                              ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '15', '11', '13', '14', '-', '12'),
                              ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '-', '11', '13', '14', '15', '12'),
                              ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '-', '13', '14', '15', '12'),
                              ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '-')]

        self.assertEqual(oikeat_valivaiheet, ohjelma.valivaiheet())

    def test_oikea_ratkaisu_1(self):
        aloitustilanne =  ('-', '2', '3', '4', '1', '6', '7', '8', '5', '9', '10', '12', '13', '14', '11', '15')
        ohjelma = Ratkaisuohjelma(aloitustilanne)

        oikea_ratkaisu = ['1', '5', '9', '10', '11', '15']
        saatu_ratkaisu = ohjelma.ratkaisu()

        self.assertEqual(oikea_ratkaisu, saatu_ratkaisu)

    def test_oikea_ratkaisu_2(self):
        aloitustilanne =  ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '15', '-', '13', '14', '12', '11')
        ohjelma = Ratkaisuohjelma(aloitustilanne)

        oikea_ratkaisu = ['11', '12', '15', '11', '12']
        saatu_ratkaisu = ohjelma.ratkaisu()

        self.assertEqual(oikea_ratkaisu, saatu_ratkaisu)
