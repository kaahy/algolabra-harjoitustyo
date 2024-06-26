class Ratkaisuohjelma():
    def __init__(self, aloitustilanne):
        self.aloitustilanne = aloitustilanne

        self.vaiheet = []
        self.siirtojarjestys = None
        self.ratkaistu = False

    def ratkaisu(self):
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
        return self.vaiheet

    def paivita_siirtojarjestys(self, vaiheet):
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

    def onko_ratkaistavissa(self, tilanne):
        inversioiden_maara = self.laske_inversiot(tilanne)
        tyhjan_rivinro = tilanne.index('-') // 4

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
        # millaiset laattajärjestykset mahdollisia seuraavan siirron jälkeen
        # palauttaa listan tupleja (etaisyysarvio, naapuri) etäisyysarvion mukaan järjestettynä

        tilanne = list(tilanne_)
        vaihtoehdot = []

        i = tilanne_.index('-')

        # siirto oikealta
        if i not in [3, 7, 11, 15]:
            tilanne2 = tilanne.copy()
            tilanne2[i], tilanne2[i+1] = tilanne[i+1], '-'
            vaihtoehdot.append((self.laske_kustannus(tilanne2), tuple(tilanne2)))
        # siirto vasemmalta
        if i not in [0, 4, 8, 12]:
            tilanne2 = tilanne.copy()
            tilanne2[i], tilanne2[i-1] = tilanne[i-1], '-'
            vaihtoehdot.append((self.laske_kustannus(tilanne2), tuple(tilanne2)))
        # siirto ylhäältä
        if i not in [0, 1, 2, 3]:
            tilanne2 = tilanne.copy()
            tilanne2[i], tilanne2[i-4] = tilanne[i-4], '-'
            vaihtoehdot.append((self.laske_kustannus(tilanne2), tuple(tilanne2)))
        # siirto alhaalta
        if i not in [12, 13, 14, 15]:
            tilanne2 = tilanne.copy()
            tilanne2[i], tilanne2[i+4] = tilanne[i+4], '-'
            vaihtoehdot.append((self.laske_kustannus(tilanne2), tuple(tilanne2)))

        vaihtoehdot.sort()

        return vaihtoehdot

    def manhattan_distance(self, tilanne):
        #summa laattojen etäisyyksistä oikeilta paikoiltaan

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

        return etaisyyksien_summa

    def laske_kustannus(self, tilanne):
        # heuristinen etäisyysarvio (jäljellä olevat siirrot)
        # tilapäisesti yksinkertainen

        return self.manhattan_distance(tilanne)

    def ida_syvyyshaku(self, solmu, reitti, kustannusarvio, siirtoja=0):
        fscore = siirtoja + kustannusarvio

        reitti2 = reitti.copy()
        reitti2.append(solmu)

        if self.ratkaistu:
            return
        if self.onko_ratkaisu(solmu):
            self.vaiheet = reitti2
            self.ratkaistu = True
            return

        self.laskuri -= 1
        if self.laskuri < 0:
            return

        if fscore > self.iteraation_treshold:
            self.seuraavan_iteraation_treshold = min(self.seuraavan_iteraation_treshold, fscore)
            return

        for naapuri in self.naapuritilanteet(solmu):
            if naapuri[1] not in reitti:
                self.ida_syvyyshaku(naapuri[1], reitti2, naapuri[0], siirtoja+1)

    def ida_algoritmi(self, aloitustilanne):
        aloitustilanteen_etaisyysarvio = self.laske_kustannus(aloitustilanne)
        self.iteraation_treshold = aloitustilanteen_etaisyysarvio
        self.laskuri = 50000000 # ettei etsitä liian kauan, jos ratkaisua ei löydy

        # iteraatioita kunnes ratkaisu löytynyt, aina alkusolmusta aloittaen
        while True:
            self.seuraavan_iteraation_treshold = 100000 # päivittyy tämän iteraation aikana

            self.ida_syvyyshaku(aloitustilanne, [], aloitustilanteen_etaisyysarvio)

            if self.ratkaistu:
                self.paivita_siirtojarjestys(self.vaiheet)
                return

            self.iteraation_treshold = self.seuraavan_iteraation_treshold

            if self.laskuri < 0:
                return
