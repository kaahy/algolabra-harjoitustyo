# Käyttöohjeet

## Aloitus
1. Kloonaa projekti koneellesi.
2. Siirry komentorivillä projektin juurihakemistoon.
3. Asenna riippuvuudet komennolla `poetry install`.

## Käyttö

1. Käynnistä ohjelma komennolla `python3 src/index.py`.
2. Syötä 15-pelin aloitusruudukon numerot yhtenä merkkijonona pilkuin eroteltuina, aloittaen ylärivistä vasemmalta. Merkitse tyhjä ruutu viivalla. Esimerkkisyöte: 1,10,6,4,5,2,15,3,9,7,12,8,13,-,14,11

## Testaus

1. Aktivoi virtuaaliympäristö komennolla `poetry shell`.
2. Suorita testit komennolla `coverage run --branch -m pytest src` (tai jos haluat vain suorittaa testit tekemättä sen jälkeen alla mainittuja coverage-toimintoja, myös pelkkä komento `pytest` riittää).
- Testikattavuuden näet komennolla `coverage report -m`.
- Testikattavuusraporttia voit tarkastella selaimessa, kun annat komennon `coverage html` ja avaat sitten projektin hakemistoon ilmestyneen tiedoston *htmlcov/index.html*.

## Pylint-laatutarkistukset

Anna virtuaaliympäristössä komento `pylint src`.
