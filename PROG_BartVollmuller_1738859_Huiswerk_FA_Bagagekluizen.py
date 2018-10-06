def toon_aantal_kluizen_vrij():
    file = open("Bagagekluizen.txt", "r") # Hiermee wordt het bestand geopend en kan er worden geschreven.
    regels = 12 - len(file.readlines())
    file.close()
    return regels

def nieuwe_kluis(wachtwoord):
    kluis = abs(toon_aantal_kluizen_vrij() - 11)  # (Bij 0 is er geen kluis) Met deze functie ziet het programma welke kluis de volgende beschikbare kluis moet zijn
    file = open("Bagagekluizen.txt", "a")
    file.write(str(kluis) + ";" + str(wachtwoord) + "\n")

def kluis_openen(kluisnummer):
    kluisnummer = kluisnummer - 1  #Hiermee wordt de invoer met optie 0 veranderd in optie 1.
    file = open("Bagagekluizen.txt", "r")
    kluisinvoer = file.readlines()
    kluisinvoer = kluisinvoer[int(kluisnummer)]
    file.close()
    return kluisinvoer

def mooieopmaak():  #Dit zorgt er simpelweg voor dat er een aantal enters tussen 1e en 2e run van het programma.
    print("\t")
    print("\t")
    print("\t")
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

        if optie == 1: #Als deze optie wordt geselecteerd, wordt vermeld hoeveel kluizen er vrij zijn.
            print("In totaal zijn er", toon_aantal_kluizen_vrij(), "kluizen vrij.")
            mooieopmaak()

        elif optie == 2: #Als deze optie wordt geselecteerd, wordt er gevraagd om een wachtwoord te maken en wordt deze vervolgens toonbaar gesteld aan de user.
            if toon_aantal_kluizen_vrij() > 0:
                invoer = eval(input("Typ hier uw wachtwoord:"))
                kluis = abs(toon_aantal_kluizen_vrij() - 11)
                print("Uw kluisnummer is:" + str(kluis))
                print("Uw opgegeven wachtwoord is:" + str(invoer))
                nieuwe_kluis(invoer)
                print("Uw kluis met uw opgegeven wachtwoord staat nu geregistreerd.")
                mooieopmaak()

            else: #Als er geen bagagekluizen beschikbaar zijn, zal er een melding komen waarbij duidelijk wordt gemaakt dat er geen kluizen beschikbaar zijn.
                print("Helaas, alle kluizen zijn op het moment in gebruik.")
                print("Excuses voor het ongemak.")
                mooieopmaak()

        elif optie == 3: #Als deze optie wordt geselecteerd, moet het kluisnummer en het kluiswachtwoord worden ingevoerd, als het wachtwoord niet gelijk is, verschijnt er een melding.
            kluisnummer = int(input("Wat is uw kluisnummer?:"))
            kluiswachtwoord = eval(input("Wat is het wachtwoord van uw kluis?:"))
            if invoer[0] == str(kluiswachtwoord):
                print("Het wachtwoord is juist.")
                mooieopmaak()
            else:
                print("U heeft het verkeerde wachtwoord ingevuld.")
                mooieopmaak()

        else:
            print("Deze optie bestaat niet")
            mooieopmaak()


except KeyboardInterrupt:
    pass