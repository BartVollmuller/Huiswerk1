def toon_aantal_kluizen_vrij():
    file = open('Bagagekluizen.txt', 'r') # Hiermee wordt het bestand geopend en kan er worden geschreven.
    regels = 12 - len(file.readlines())
    file.close()
    return regels


def nieuwe_kluis(wachtwoord):
    kluis = abs(toon_aantal_kluizen_vrij() - 11)  # (Bij 0 is er geen kluis) Met deze functie ziet het programma welke kluis de volgende beschikbare kluis moet zijn
    file = open('Bagagekluizen.txt', 'a')
    file.write(str(kluis) + ";" + str(wachtwoord) + "\n")


def kluis_openen(kluisnummer):
    kluisnummer = kluisnummer - 1  # zo ziet het systeem kluis 1 wel als kluis nul maar laat dat niet zien
    file = open('Bagagekluizen.txt', 'r')
    invoer = file.readlines()
    invoer = invoer[int(kluisnummer)]
    file.close()
    return invoer


def whitespace():  # door deze functie zie je duidelijk waarneer het programma weer opnieuw begint, en zie je de output van je vorige command duidelijker
    print("\t")
    print("\t")
    print("\t")


try:
    while True:

        print("Optie 1: Ik wil het aantal beschikbare kluizen weten.")
        print("Optie 2: Ik wil een nieuwe kluis.")
        print("Optie 3: Ik wil mijn kluis openen.")
        print("")


        optie = (int(input("Kies een optie:")))

        if optie == 1:
            print("In totaal zijn er", toon_aantal_kluizen_vrij(), "kluizen vrij.")
            whitespace()


        elif optie == 2:
            if toon_aantal_kluizen_vrij() > 0:
                invoer = eval(input("Voor uw ingestelde wachtwoord in:"))
                kluis = abs(toon_aantal_kluizen_vrij() - 11)
                print("Uw kluisnummer is:" + str(kluis))
                print("Uw opgegeven wachtwoord is:" + str(invoer))
                nieuwe_kluis(invoer)
                print("Uw kluis met wachtwoord staat nu geregistreerd")
                whitespace()




            else:
                print("Helaas, alle kluizen zijn op het moment in gebruik")
                print("Excuses voor het ongemak")
                whitespace()






        elif optie == 3:
            kluisnummer = int(input("Wat is uw kluisnummer?:"))
            kluiswachtwoord = eval(input("Wat is het wachtwoord van uw kluis?:"))
            if invoer[0] == str(kluiswachtwoord):
                print("Het wachtwoord is juist.")
                whitespace()
            else:
                print("U heeft het verkeerde wachtwoord ingevuld.")
                whitespace()







        else:
            print("Deze optie bestaat niet")
            whitespace()

except KeyboardInterrupt:
    pass
