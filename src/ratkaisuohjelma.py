class Ratkaisuohjelma():
    def __init__(self, aloitustilanne=None):
        self.aloitustilanne = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '-', '13', '14', '15']

        #self.vaiheet = []
        #self.siirtojarjestys = []
        #self.ratkaistu = False

        # alussa nämä, kun ohjelma ei vielä toimi
        self.vaiheet =  [['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '-', '13', '14', '15'],
                         ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '-', '14', '15'],
                         ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '-', '15'],
                         ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '-']]
        self.siirtojarjestys = [13, 14, 15]
        self.ratkaistu = True

    def ratkaisu(self):
        if not self.onko_ratkaistavissa(self.aloitustilanne):
            return None
        if self.onko_ratkaisu(self.aloitustilanne):
            return []
        if self.ratkaistu:
            return self.siirtojarjestys

        #self.ida_algoritmi(self.aloitustilanne)

        return self.siirtojarjestys

    def valivaiheet(self):
        return self.vaiheet

    def onko_ratkaisu(self, tilanne):
        if tilanne == ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '-']:
            return True
        return False

    def onko_ratkaistavissa(self, tilanne):
        inversioiden_maara = self.laske_inversiot(tilanne)
        tyhjan_rivinro = tilanne.index('-') // 4

        if (inversioiden_maara + 1+tyhjan_rivinro) % 2 == 0:
            return True

        return False

    def laske_inversiot(self, tilanne):
        inversiot_lkm = 0

        for ai in range(len(tilanne)-1):
            a = tilanne[ai]
            if a != '-':
                for bi in range(ai+1, len(tilanne)):
                    b = tilanne[bi]
                    if b != '-':
                        if int(b) < int(a):
                            inversiot_lkm += 1

        return inversiot_lkm

    def naapuritilanteet(self, tilanne):
        # millaiset laattajärjestykset mahdollisia seuraavan siirron jälkeen
        vaihtoehdot = []

        for i in range(len(tilanne)):
            laatta = tilanne[i]

            if laatta == '-':
                # siirto oikealta
                if i not in [3, 7, 11, 15]:
                    tilanne2 = tilanne.copy()
                    tilanne2[i] = tilanne[i+1]
                    tilanne2[i+1] = '-'
                    vaihtoehdot.append(tilanne2)
                # siirto vasemmalta
                if i not in [0, 4, 8, 12]:
                    tilanne2 = tilanne.copy()
                    tilanne2[i] = tilanne[i-1]
                    tilanne2[i-1] = "-"
                    vaihtoehdot.append(tilanne2)
                # siirto ylhäältä
                if i not in [0, 1, 2, 3]:
                    tilanne2 = tilanne.copy()
                    tilanne2[i] = tilanne[i-4]
                    tilanne2[i-4] = '-'
                    vaihtoehdot.append(tilanne2)
                # siirto alhaalta
                if i not in [12, 13, 14, 15]:
                    tilanne2 = tilanne.copy()
                    tilanne2[i] = tilanne[i+4]
                    tilanne2[i+4] = '-'
                    vaihtoehdot.append(tilanne2)
                break

        return vaihtoehdot

    def laske_kustannus(self, tilanne):
        # heuristinen etäisyysarvio
        pass

    def ida_algoritmi(self, tilanne):
        pass
