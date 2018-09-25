leeftijd = int(input("Geef je leeftijd"))
paspoort = str(input("Heb je een Nederlands paspoort?"))
if leeftijd >=18 and paspoort == "Ja":
    print("Gefeliciteerd je mag stemmen!")
else:
    print("Je mag nu nog niet stemmen!")
