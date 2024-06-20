import time
from ratkaisuohjelma import Ratkaisuohjelma

def tarkista_syote(syote):
    syote_listana = syote.split(',')
    if sorted(syote_listana) == sorted(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '-']):
        return True
    return False

def main():
    print("________________________________________\n")
    print("15-PELIN RATKAISUOHJELMA\n")
    print("HUOM. Ohjelma ratkaisee tällä hetkellä vain helpoimpia pelitilanteita.\n")

    while True:
        syote = input("Syötä aloitustilanne (esim. 1,-,2,4,5,6,3,8,9,10,7,11,13,14,15,12):\n")
        if tarkista_syote(syote):
            break
        print("\nVirheellinen syöte. Yritä uudelleen.\n")

    aloitustilanne = tuple(syote.split(','))

    ohjelma = Ratkaisuohjelma(aloitustilanne)
    aloitusaika = time.time()
    ratkaisu = ohjelma.ratkaisu()
    lopetusaika = time.time()
    valivaiheet = ohjelma.valivaiheet()

    print('\nRATKAISU:\n')

    if ratkaisu is None:
        if not ohjelma.onko_ratkaistavissa(aloitustilanne):
            print("Syöttämällesi pelille ei ole olemassa ratkaisua.\n")
        else:
            print("Syöttämällesi pelille ei onnistuttu löytämään ratkaisua.\n")
    else:
        print(f"Siirtojärjestys ({len(ratkaisu)} siirtoa): {', '.join(ratkaisu)}\n")
        print("Välivaiheet:\n")
        tulosta_taulukot(valivaiheet)
        print(f"Aikaa meni {lopetusaika-aloitusaika} sekuntia.\n")

    print("________________________________________\n")

def tulosta_taulukot(valivaiheet):
    for tilanne in valivaiheet:
        print(tilanne[0], tilanne[1], tilanne[2], tilanne[3], sep="\t")
        print(tilanne[4], tilanne[5], tilanne[6], tilanne[7], sep="\t")
        print(tilanne[8], tilanne[9], tilanne[10], tilanne[11], sep="\t")
        print(tilanne[12], tilanne[13], tilanne[14], tilanne[15], sep="\t")
        print()

main()
