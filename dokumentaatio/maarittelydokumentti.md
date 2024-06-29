# Määrittelydokumentti

Toteutan projektin Helgingin yliopiston Algoritmit ja tekoäly -harjoitustyökurssilla, jonka suoritan osana tietojenkäsittelytieteen kandiohjelmaa.

## Projektin perustiedot

**Ratkaistava ongelma:** 15-pelin optimaalinen ratkaisu. 15-pelin päämäärä on siirrellä 4x4-ruudukossa olevat laatat numerojärjestykseen, ja optimaalisessa ratkaisussa siirtoja on mahdollisimman vähän.

**Ohjelman toiminta käyttäjän näkökulmasta:** Käyttäjä syöttää pelin alkutilanteen yhtenä merkkijonoja, esim. 1,2,12,14,7,3,15,11,8,9,-,5,10,6,4,13, jossa viiva tarkoittaa tyhjää ruutua. Numerot luetellaan riveittäin ylhäältä alas ja vasemmalta oikealle. Ohjelma tulostaa ratkaisun sekä merkkijonona, jossa luetellaan siirrettävät laatat järjestyksessä, että taulukkoina pelin välivaiheista. Ohjelma toimii komentorivikäyttöliittymällä.

**Ohjelmointikielet:** Python (myös vertaisarvioitavissa projekteissa).

**Algoritmit:** IDA* (Iterative deepening A*), jonka tilavaativuus on O(d).

## Projektin ydin

Projektissa tärkeintä on koodi, jolla saadaan 15-peliin ratkaisuja mahdollisimman vähillä siirroilla. Ongelma on NP-täydellinen, eli sitä ei voi ratkaista tehokkaasti. On kuitenkin olemassa heuristiikoita, joilla saadaan tarvittavien siirtojen vähimmäismäärälle alarajoja. Lisäksi voidaan yhdistellä aiemmin laskettuja ja tallennettuja osaratkaisuja. Koodissa 15-peliä käsitellään verkkona, johon sovelletaan IDA*-reitinhakualgoritmia. IDA* ratkaisee mahdollisimman lyhyen reitin lähtösolmusta päätössolmuun heuristiikkojen avulla.

**15-peli verkkona:** 15-pelin tapauksessa verkon solmut vastaavat pelin eri tilanteita. Esimerkiksi lähtösolmu vastaa pelin aloitustilannetta. Sen naapurisolmut vastaavat tilanteita, jossa peli voi seuraavan siirron jälkeen olla. Maalisolmu vastaa pelin lopetustilannetta eli ratkaisua.

**IDA\*-algoritmin toimintaperiaate:** IDA\* käy verkon solmuja läpi iteraatioittain syvemmälle etenevinä syvyyshakuina valiten solmun naapurisolmuista aina ensin sen, jonka valitessaan arvioitu kokonaiskustannus  (15-pelin tapauksessa siirtojen määrä) olisi pienin. Jokaisen vaihtoehdon arvioitu kokonaiskustannus saadaan laskemalla yhteen todellinen kustannus vaihtoehtosolmuun asti ja heuristiikkojen avulla arvioitu sen jälkeinen kustannus.

## Lähteitä

- [https://en.wikipedia.org/wiki/Iterative_deepening_A*](https://en.wikipedia.org/wiki/Iterative_deepening_A*)
- https://michael.kim/blog/puzzle
