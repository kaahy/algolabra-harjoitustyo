# Testausdokumentti

## Yksikkötestauksen kattavuusraportti

File | statements | missing | excluded | branches | partial | coverage
-----|---|---|---|---|---|-----
src/ratkaisuohjelma.py | 124 | 8 | 0 | 48 | 5 | 91%
Total | 124 | 8 | 0 | 48 | 5 | 91%

## Mitä on testattu

### Yksikkötestit

Kaikki yksikkötestit testaavat Ratkaisuohjelma-luokkaa.

- Ohjelma selvittää oikein kaikki pelitilanteet, jotka tietystä pelitilanteesta on mahdollista seurata yhden siirron jälkeen.
  - Tätä varten on usea testi, jossa kussakin tyhjä ruutu on eri kohdassa (vasemmassa yläkulmassa, oikeassa laidassa jne.) ja siis myös mahdollisten seuraavien pelitilanteiden määrä vaihtelee.
- Ohjelma selvittää oikein, onko pelille olemassa ratkaisua.
  - Testattavana pelitilanteena, jolle on olemassa ratkaisu, on aloitustilanne oikeasta nettipelistä.
  - Testattavana pelitilanteena, jolle ei ole olemassa ratkaisua, on 15-pelin Wikipedia-artikkelista löytyvä esimerkki ratkaisemattomasta pelistä.
- Ratkaisu on None, jos ratkaisua ei ole olemassa.
  - Testattava pelitilanne on sama kuin edellä.
- Ohjelma laskee pelitilanteen inversioiden määrän oikein.
  - Testattavassa tilanteessa inversiot on laskettu manuaalisesti.
- Ohjelman antama ratkaisu on mahdollisimman lyhyt.
  - Testattavana on yksinkertainen pelitilanne, jonka voi ratkaista siirtämällä tyhjän ruudun lyhyintä reittiä vasemmasta ylänurkasta oikeaan ylänurkkaan ja siitä oikeaan alanurkkaan, eli sen lyhyimmässä ratkaisussa on 6 siirtoa.
- Ratkaisu on oikein.
   - Välivaiheiden oikeellisuutta on testattu kahdella itse sekoitetulla yksinkertaisella pelitilanteella, joiden välivaiheet on kirjattu manuaalisesti.
   - Siirtojärjestyksen oikeellisuutta on testattu samoilla aloitustilanteilla kuin edellä.
- Ratkaisu on tyhjä lista, jos aloitustilanne on jo ratkaisu.
- Heuristiikka "manhattan distance" toimii oikein, eli se palauttaa se summan, joka saadaan laskemalla yhteen kunkin laatan etäisyys ratkaisutilanteen ruudustaan.
  - Testattavana on pari yksinkertaista pelitilannetta, joiden MD on laskettu manuaalisesti.

#### Testien suoritus

- Siirry ensin virtuaaliympäristöön: **poetry shell**
- Suorita testit: **coverage run --branch -m pytest src**
- Näe testikattavuus: **coverage report -m**
- Luo tai päivitä selaimessa katsottava testikattavuusraportti (htmlcov/index.html): **coverage html**

### Käyttöliittymän testaus

Käyttöliittymän toimivuutta on manuaalisesti havainnoitu jatkuvasti kehityksen aikana. Esimerkkejä testeistä:

- Jos käyttäjän syöte on virheellinen, ohjelma tulostaa virheestä ilmoituksen ja antaa yrittää uudelleen.
  - Testisyötteitä: tyhjä syöte, välilyönti, "a", "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15" (viiva puuttuu) ja "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15,-" (kaksi samaa numeroa).
- Jos syötettä vastaavalle pelille ei ole ratkaisua (mutta syöte on muuten oikein), ohjelma kertoo tästä.
  - Testisyöte: "13,9,5,1,14,10,6,2,15,11,7,3,-,12,8,4". Tämä peli tiedetään Wikipedian 15-peli-artikkelin perusteella mahdottomaksi ratkaista.
- Jos syötetylle pelille on olemassa ratkaisu (ja ohjelma tulostaa sen nopeasti), tulostuksessa näkyy mitä pitääkin, eli siirtojärjestys, siirtojen määrä, välivaiheet aloitus- ja ratkaisutilanne mukaan lukien, ratkaisuohjelma käyttämä aika ja tiedot vierailtujen solmujen määrästä. Siirtojärjestys ja välivaiheet myös vastaavat toisiaan ja todellisuutta.
  - Testisyötteitä: "1,2,3,4,5,6,7,8,9,10,11,12,13,14,-,15" (1 siirto eli 2 välivaihetta) ja "1,2,3,4,5,6,7,8,9,10,11,12,-,13,14,15" (3 siirtoa eli 4 välivaihetta).
  - Edellisen lisäksi on testattu, että jos syöte on jo valmiiksi ratkaisu ("1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,-"), ohjelman tulostama siirtojärjestys on tyhjä, siirtojen määrä 0 ja välivaiheina vain yksi tilanne.
