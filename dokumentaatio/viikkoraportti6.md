# Viikkoraportti 6

Viikko kesken...

## Maanantai

Tunnin Zoom-keskustelu ohjaajan kanssa. Sain vinkkejä työn parantamiseen. Tärkeimpänä ohjeena sain korjata solmujen vierailujärjestyksen. Algoritmi käy tällä hetkellä naapurisolmut vain jossain oletusjärjestyksessä, vaikka ne pitäisi käydä etäisyysarvioiden mukaisessa järjestyksessä aloittaen siitä, mistä on arviolta vähiten siirtoja jäljellä. Myöhemmin yritin korjata tätä, mutta jostain syystä ohjelmasta tulikin sen myötä hitaampi. Koodissa on varmaan bugi, tai ehkä olen myös ymmärtänyt jotain väärin. Pitää vielä perehtyä tähän lisää ja yrittää uudestaan.

Yritimme Zoom-keskustelussa myös tutkia missä vaiheessa ohjelma alkaa käydä liian hitaaksi, syöttämällä sille manuaalisesti sekoittamiani pelitilanteita. Emme kuitenkaan ehtineet löytää sellaista kohtaa, joten jatkoin tätä keskustelun jälkeen itsenäisesti. Huomasin esimerkiksi, että ohjelma antoi yhteen syötteeseen (-,10,4,15,2,7,6,12,1,13,3,11,5,9,8,14) ratkaisuksi 42 siirtoa hieman alle sekunnissa. Enemmän sekoittamaani syötteeseen (10,7,4,15,-,13,6,12,2,1,3,11,5,9,8,14) ohjelma antoi ratkaisuksi 51 siirtoa noin 12 sekunnissa. Kun sekoitin viimeksi mainittua lisää yhden siirron verran (syöte 10,7,4,15,13,-,6,12,2,1,3,11,5,9,8,14), ohjelma ei onnistunut ratkaisemaan sitä ainakaan odottamani yli 3 minuutin aikana. Ohjelmassa on tällä hetkellä (ei ajallinen) rajoitus sille, kauanko se voi etsiä ratkaisua. Testasin näitä syötteitä niin, että olin kommentoinut rajoituksen pois.

Tavoite olisi saada ohjelma nopeutumaan niin, että ratkaisuajassa huomaisi selvän parannuksen edellä mainittuihin tuloksiin verrattuna. Ohjelmaa voisi nopeuttaa myös etäisyysarvion laskemistavan muutoksella. Tämä hetken ajatukseni on käyttää lopullisessa versiossa pelkän manhattan distance -heurustiikan sijaan manhattan distancen ja iteration distancen maksimia. Kuitenkin ohjaajan puheista käsitin, että solmujen läpikäyntijärjestys vaikuttaisi nopeuteen vielä enemmän.

Tein pieniä muutoksia käyttöliittymään: Se tulostaa nyt ratkaisuun menneen ajan sekä siirtojen määrän, jotta niitä ei tarvitse laskea itse. Lisäksi käyttöliittymä ilmoittaa nyt selkeämmin, jos peliin ei ole olemassa ratkaisua. (Aiemmin se tulosti saman ilmoituksen riippumatta siitä, oliko peli ratkaisematon vai eikö ohjelma vain onnistunut löytämään ratkaisua.)

3,5 tuntia.

## Tiistai

Tutustuin alustavasti kurssin toiseen vertaisarvioitavaan projektiin Githubin kautta. En kloonannut sitä vielä. 40 min.

## Keskiviikko

- Vertaisarvioitavan projektin kloonaus, ohjelman kokeilu ja koodiin tutustumien.
- Tulossa...

(Kesken...)
