class Ratkaisuohjelma():
    """15-pelin ratkaistavuuden ja lyhyimmän ratkaisun selvittämisestä vastaava luokka."""

    def __init__(self, aloitustilanne):
        """Args:
            aloitustilanne (tuple): esim. ('1', '10', '6', '4', '5', '2', '15', '3', '9', '7', '12', '8', '13', '-', '14', '11')
        """
        self.aloitustilanne = aloitustilanne

        self.vaiheet = []
        self.siirtojarjestys = None
        self.ratkaistu = False

        self.vierailulaskuri = 0
        
        self.naapurimuisti = {}
        self.md_muisti = {}

    def ratkaisu(self):
        """Palauttaa siirtojärjestyksen listana numeroita, jos ratkaisu löytyy, muutoin None."""
        if not self.onko_ratkaistavissa(self.aloitustilanne):
            return None
        if self.onko_ratkaisu(self.aloitustilanne):
            self.vaiheet = [self.aloitustilanne]
            return []
        if self.ratkaistu:
            return self.siirtojarjestys

        self.ida_algoritmi(self.aloitustilanne)

        return self.siirtojarjestys

    def valivaiheet(self):
        """Palauttaa välivaiheet listana tupleja, ml. aloitus- ja ratkaisutilanteet."""
        return self.vaiheet

    def paivita_siirtojarjestys(self, vaiheet):
        """Asettaa self.siirtojarjestys-muuttujaan välivaiheista lasketun siirtojärjestyksen listana numeroita."""
        if not self.ratkaistu:
            return

        siirrettavat_numerot = []

        tyhjan_sijainti = vaiheet[0].index('-')

        for vaihe in self.vaiheet[1:]:
            tyhjaan_siirretty_numero = vaihe[tyhjan_sijainti]
            siirrettavat_numerot.append(tyhjaan_siirretty_numero)
            tyhjan_sijainti = vaihe.index('-')

        self.siirtojarjestys = siirrettavat_numerot

    def onko_ratkaisu(self, tilanne):
        return tilanne == ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '-')

    def onko_ratkaistavissa(self, aloitustilanne):
        """Palauttaa tiedon (True/False), onko pelille olemassa ratkaisua."""
        inversioiden_maara = self.laske_inversiot(aloitustilanne)
        tyhjan_rivinro = aloitustilanne.index('-') // 4

        return (inversioiden_maara + 1+tyhjan_rivinro) % 2 == 0

    def laske_inversiot(self, tilanne):
        inversiot_lkm = 0

        for a_i, a in enumerate(tilanne[:-1]):
            if a == '-':
                continue
            for b in tilanne[a_i+1:]:
                if b != '-':
                    inversiot_lkm += int(b) < int(a)

        return inversiot_lkm

    def naapuritilanteet(self, tilanne_):
        """Selvittää millaiset laattajärjestykset ovat mahdollisia seuraavan siirron jälkeen.
        Palauttaa listan tupleja (etaisyysarvio, naapuri) etäisyysarvion mukaan järjestettynä.
        """
        if tilanne_ in self.naapurimuisti:
            return self.naapurimuisti[tilanne_]

        tilanne = list(tilanne_)
        vaihtoehdot = []

        i = tilanne_.index('-')

        # siirto oikealta
        if i not in [3, 7, 11, 15]:
            tilanne2 = tilanne.copy()
            tilanne2[i], tilanne2[i+1] = tilanne[i+1], '-'
            vaihtoehdot.append((self.arvio_tulevista_siirroista(tilanne2), tuple(tilanne2)))
        # siirto vasemmalta
        if i not in [0, 4, 8, 12]:
            tilanne2 = tilanne.copy()
            tilanne2[i], tilanne2[i-1] = tilanne[i-1], '-'
            vaihtoehdot.append((self.arvio_tulevista_siirroista(tilanne2), tuple(tilanne2)))
        # siirto ylhäältä
        if i not in [0, 1, 2, 3]:
            tilanne2 = tilanne.copy()
            tilanne2[i], tilanne2[i-4] = tilanne[i-4], '-'
            vaihtoehdot.append((self.arvio_tulevista_siirroista(tilanne2), tuple(tilanne2)))
        # siirto alhaalta
        if i not in [12, 13, 14, 15]:
            tilanne2 = tilanne.copy()
            tilanne2[i], tilanne2[i+4] = tilanne[i+4], '-'
            vaihtoehdot.append((self.arvio_tulevista_siirroista(tilanne2), tuple(tilanne2)))

        vaihtoehdot.sort()

        self.naapurimuisti[tilanne_] = vaihtoehdot

        return vaihtoehdot

    def manhattan_distance(self, tilanne):
        """Palauttaa summan (int) laattojen etäisyyksistä oikeilta paikoiltaan."""
        if tilanne in self.md_muisti:
            return self.md_muisti[tilanne]

        etaisyyksien_summa = 0

        for i in range(16):
            numero = tilanne[i]

            if numero == '-':
                continue

            rivi = i // 4
            sarake = i - (rivi) * 4

            oikea_kohta = int(numero) - 1
            oikea_rivi = (oikea_kohta) // 4
            oikea_sarake = oikea_kohta - (oikea_rivi) * 4

            rivietaisyys = abs(rivi - oikea_rivi)
            sarakeetaisyys = abs(sarake - oikea_sarake)

            etaisyyksien_summa += rivietaisyys + sarakeetaisyys

        self.md_muisti[tilanne] = etaisyyksien_summa

        return etaisyyksien_summa

    def arvio_tulevista_siirroista(self, tilanne):
        """Heuristinen arvio (int) sille, mikä tulevien siirtojen pienin määrä enintään olisi."""
        return self.manhattan_distance(tuple(tilanne))

    def ida_syvyyshaku(self, tilanne, reitti, arvio_tulevista_siirroista, siirtoja=0):
        """Solmuissa vierailua. Yksi pelitilanne vastaa yhtä solmua."""
        self.vierailulaskuri += 1

        reitti2 = reitti.copy()
        reitti2.append(tilanne)

        if self.ratkaistu:
            return
        if self.onko_ratkaisu(tilanne):
            self.vaiheet = reitti2
            self.ratkaistu = True
            return

        self.laskuri -= 1
        if self.laskuri < 0:
            return

        # jos vähimmäissiirtojen kokonaismääräarvio (fscore) on tälle tilanteelle/solmulle liian suuri (> treshold), solmua ei tutkita enempää nykyisessä iteraatiossa
        fscore = siirtoja + arvio_tulevista_siirroista
        if fscore > self.iteraation_treshold:
            # seuraavan iteraation treshold tulee olemaan pienin fscore niiltä solmuilta, joiden fscore nykyisessä iteraatiossa ylittää tresholdin
            self.seuraavan_iteraation_treshold = min(self.seuraavan_iteraation_treshold, fscore)
            return

        for naapuri in self.naapuritilanteet(tilanne):
            if naapuri[1] not in reitti:
                self.ida_syvyyshaku(naapuri[1], reitti2, naapuri[0], siirtoja+1)

    def ida_algoritmi(self, aloitustilanne):
        """Etsii ratkaisua ja sen löytyessä päivittää konstruktorin ratkaisumuuttujat."""
        aloitustilanteen_etaisyysarvio = self.arvio_tulevista_siirroista(aloitustilanne)
        self.iteraation_treshold = aloitustilanteen_etaisyysarvio # fscoren ylärajoitus, kasvaa iteraatioittain
        self.laskuri = 50000000 # ettei etsitä liian kauan, jos ratkaisua ei löydy

        # iteraatioita kunnes ratkaisu löytynyt, aina alkusolmusta aloittaen
        # joka iteraatiolla edetään solmuissa (pelitilanteissa) syvemmälle kuin edellisellä
        while True:
            self.seuraavan_iteraation_treshold = 100000

            self.ida_syvyyshaku(aloitustilanne, [], aloitustilanteen_etaisyysarvio)

            if self.ratkaistu:
                self.paivita_siirtojarjestys(self.vaiheet)
                return

            self.iteraation_treshold = self.seuraavan_iteraation_treshold

            if self.laskuri < 0:
                return
