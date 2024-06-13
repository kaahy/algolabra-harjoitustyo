# Testausdokumentti

## Yksikkötestauksen kattavuusraportti

File | statements | missing | excluded | branches | partial | coverage
-----|---|---|---|---|---|-----
src/ratkaisuohjelma.py | 130 | 7 | 0 | 58 | 7 | 93%
Total | 130 | 7 | 0 | 58 | 7 | 93%

## Mitä on testattu

Kaikki testit ovat yksikkötestejä.


- Selvittääkö ohjelma oikein kaikki pelitilanteet, jotka tietystä pelitilanteesta on mahdollista seurata yhden siirron jälkeen
  - Tätä varten on usea testi, jossa kussakin tyhjä ruutu on eri kohdassa (vasemmassa yläkulmassa, oikeassa laidassa jne.) ja siis myös mahdollisten seuraavien pelitilanteiden määrä vaihtelee.
- Selvittääkö ohjelma oikein, onko pelille olemassa ratkaisua
  - Testattavana pelitilanteena, jolle on olemassa ratkaisu, on aloitustilanne oikeasta nettipelistä.
  - Testattavana pelitilanteena, jolle ei ole olemassa ratkaisua, on 15-pelin Wikipedia-artikkelista löytyvä esimerkki ratkaisemattomasta pelistä.
- Laskeeko ohjelma pelitilanteen inversioiden määrän oikein
  - Testattavassa tilanteessa inversiot on laskettu manuaalisesti.
- Onko ohjelman antama ratkaisu on mahdollisimman lyhyt
  - Testattavana on yksinkertainen pelitilanne, jonka voi ratkaista siirtämällä tyhjän ruudun lyhyintä reittiä vasemmasta ylänurkasta oikeaan ylänurkkaan ja siitä oikeaan alanurkkaan, eli sen lyhyimmässä ratkaisussa on 6 siirtoa.
- Toimiiko alustava heurustiikka "manhattan distance" oikein, eli palauttaako se summan, joka saadaan laskemalla yhteen kunkin laatan etäisyys ratkaisutilanteen ruudustaan
  - Testattavana on pari yksinkertaista pelitilannetta, joiden MD on laskettu manuaalisesti

Testejä olisi vielä hyvä kehittää kattamaan eri pelitilanteita monipuolisemmin.

## Testauskomennot

- Siirry ensin virtuaaliympäristöön: **poetry shell**

- Suorita testit: **coverage run --branch -m pytest src**
- Näe testikattavuus: **coverage report -m**
- Luo tai päivitä selaimessa katsottava testikattavuusraportti (htmlcov/index.html): **coverage html**
