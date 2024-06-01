# Viikkoraportti 3

Tällä viikolla lisäsin metodeja ja testejä.

## Keskiviikko

Keskiviikkona en tehnyt käytännön asioita, vaan luin ja suunnittelin. Syvensin ymmärrystä IDA*-algoritmista törmäten mm. käsitteisiin f-score (verkon solmukohtainen etäisyysarvio lähtösolmusta maalisolmuun) ja treshold (rajoittaa sitä, voiko jostain solmusta edetä menossa olevalla kierroksella). Jälkimmäisen laskutapa on tässä vaiheessa epäselvä, mutta alkoi avautua myöhemmin tällä viikolla. Luin vähän kurssimateriaalia esim. testeistä. Suunnittelin metodeja ja testejä muistiinpanojen muodossa. 3,5 tuntia.

## Torstai

Viikkoraportin aloitus, eilisten suunnitelmien koodaamista, tuloksena jotain enemmän ja vähemmän järkevää. Eilinen suunnittelu helpotti työtä, mutta silti olisi ehkä kannattanut suunnitella vielä enemmän, esimerkiksi lopettaa koodaus hetkeksi ja keskittyä välillä vain suunnittelemiseen. 3 tuntia.

## Lauantai

IDA*-algoritmiin tarkemmin perehtymistä. En aiemmin ymmärtänyt, miten tässä algoritmissa toteutaan eri kierrokset. Tajusin vasta nyt, että tässä algoritmissa kierrokset ovat sellaisia, että verkon solmujen läpikäynti aloitetaan aina uudestaan alusta edeten joka kierroksella pitemmälle kuin edellisellä kierroksella. Joka kierroksella otetaan ylös uudet solmut, joihin on edetty mutta joista ei päästy eteenpäin, koska niiden f-score ylitti tresholdin. Nämä solmut on englanniksi "pruned". Näiden f-scorea vertaillaan ja pienin f-score otetaan seuraavan kierroksen tresholdiksi. Pääni on kuitenkin yhä vähän pyörällä ja jotkin yksityiskohdat kaipaavat vielä vastauksia. Esim. miten päätän aloitussolmun tresholdin? 1 tunti.

Toissapäiväisen koodiin korjailua, siistimistä ja karsimista niin että kehtaa pushata. Viikkoraportin loppuun kirjoitus. 3 tuntia.

## Aika yhteensä

10,5 tuntia.

## Seuraavaksi

En ehtinyt aloittaa kurssin viikkoaikataulussa mainittua testausdokumenttia, joten ainakin se ensi viikolla. Ja tietysti algoritmin koodaamista ja testejä. Maanantaina olisi tarkoitus osallistua testejä käsittelevään etäohjaustilaisuuteen, josta toivottavasti opin jotain hyödyllistä.
