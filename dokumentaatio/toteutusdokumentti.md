# Toteutusdokumentti

## Ohjelman yleisrakenne

Ohjelmassa on komentorivillä toimiva käyttöliittymä, johon voi syöttää 15-pelin aloitustilanteen merkkijonona. Syötteen tulee olla luvut 1 - 15 ja väliviiva missä tahansa järjestyksessä pilkuin eroteltuina niin että kutakin näistä merkeistä on tasan yksi. Jos syöte ei ollut kelvollisessa muodossa, ohjelma ilmoittaa tästä ja antaa käyttäjän yrittää uudelleen. Jos ohjelma löytää peliin ratkaisun, se tulostaa ratkaisun sekä luettelemalla laattojen numerot siirtojärjestyksessä että tulostamalla taulukot pelin välivaiheista aloitustilanteesta lopputilanteeseen. Ohjelma tulostaa myös ratkaisuohjelman käyttämän ajan ja algoritmin vierailemien solmujen määrän. Ohjelma ilmoittaa, jos pelille ei ole olemassa ratkaisua tai ohjelma ei onnistunut ratkaisemaan sitä.

Ohjelman koodi on kahdessa tiedostossa src-hakemistossa:

- **index.py** sisältää yksinkertaisen käyttöliittymän koodin, mukaan lukien syötteen tarkistuksen.
- **ratkaisuohjelma.py** sisältää luokan Ratkaisuohjelma, joka vastaa sen selvittämisestä, onko pelille olemassa ratkaisua, ratkaisun etsimisestä ja ratkaisun palauttamisesta sekä siirtojärjestyksenä että välivaiheina. Pelin ratkaistavuus selvitetään laskemalla inversioiden määrän ja tyhjän ruudun rivinumeron pariteetti. (Inversioiden määrä = monessako lukujonon lukuparissa ensimmäinen luku on jälkimmäistä suurempi.) Ratkaisua etsitään IDA*-algoritmilla, jossa hyödynnetään heuristisia etäisyysarvioita.

## Puutteita ja parannusehdotuksia

Tällä hetkellä ohjelma on monimutkaisimpien pelien ratkomisessa hyvin hidas. Ohjelmaa voisi nopeuttaa ainakin parantamalla heuristista etäisyysarviota, joka nyt arvioi tarvittavien siirtojen määrää liikaa alakanttiin. Hyvä heuristiikka aliarvioisi mahdollisimman vähän, mutta (kun kelpuutetaan vain lyhyin ratkaisu) ei koskaan yliarvioisi.

Tällä hetkellä ohjelman suoritus päättyy ohjelman tulostettua vastauksensa. Jos käyttäjä haluaa syöttää uuden pelitilanteen, hän joutuu suorittamaan ohjelman uudelleen. Käyttöliittymää voisi muuttaa niin, että käyttäjä voi jatkaa pelitilanteiden syöttämistä suoraan ja sulkea ohjelman itse.

Vertaisarvioinneista saatuja parannusehdotuksia: Laskettuja asioita, kuten etäisyyksiä ja siirtymiä, voisi tallettaa jonnekin valmiiksi. Käyttäjän manuaalisen näpyttelyn rinnalle voisi tulla arvottu syöte. Virheellisestä syötteestä tuleva ilmoitus voisi olla tarkempi.

## Laajat kielimallit

Ohjelman tekemisessä ei ole käytetty ChatGPT:tä eikä muita laajoja kielimalleja.

## Lähteitä

- https://michael.kim/blog/puzzle
- https://www.geeksforgeeks.org/iterative-deepening-a-algorithm-ida-artificial-intelligence/ (Tämä oli merkittävin lähde IDA*-algoritmin ymmärtämisessä ja koodauksessa.)
- [https://en.wikipedia.org/wiki/Iterative_deepening_A*](https://en.wikipedia.org/wiki/Iterative_deepening_A*)
- https://fi.wikipedia.org/wiki/15-peli
