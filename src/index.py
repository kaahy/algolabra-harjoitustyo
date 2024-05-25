from ratkaisuohjelma import Ratkaisuohjelma

def main():
    print("_____________________________\n")
    print("15-PELIN RATKAISUOHJELMA\n")

    print("HUOM. Tämä on vasta alustava käyttöliittymä, joka näyttää miten ohjelman on tarkoitus toimia. Ohjelma ei toimi vielä. Syötteesi ei vaikuta ohjelman toimintaan.\n")
    syote = input("Syötä aloitustilanne (esim. 1,2,3,4,5,6,7,8,9,10,11,12,-,13,14,15):\n")
    syote = '1,2,3,4,5,6,7,8,9,10,11,12,-,13,14,15' # alustavassa ei välitetä käyttäjän syötteeestä
    print()    

    aloitustilanne = syote.split(',')

    print("Pelin aloitustilanne: ", aloitustilanne, '\n')

    ######################################################################
    
    ohjelma = Ratkaisuohjelma(aloitustilanne)
    ratkaisu = ohjelma.ratkaisu()
    valivaiheet = ohjelma.valivaiheet()

    ######################################################################

    print('RATKAISU\n')

    print('Siirtojärjestys:', ratkaisu, '\n')
    
    tulosta_taulukot(valivaiheet)

    print("_____________________________\n")

def tulosta_taulukot(valivaiheet):
    for tilanne in valivaiheet:
        print(tilanne[0], tilanne[1], tilanne[2], tilanne[3], sep="\t")
        print(tilanne[4], tilanne[5], tilanne[6], tilanne[7], sep="\t")
        print(tilanne[8], tilanne[9], tilanne[10], tilanne[11], sep="\t")
        print(tilanne[12], tilanne[13], tilanne[14], tilanne[15], sep="\t")
        print()

main()
