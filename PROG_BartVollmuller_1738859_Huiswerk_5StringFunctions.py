invoerzin = input(str("Schrijf een zin:"))
splitzin = invoerzin.split(" ")
aantalzin = (len(splitzin))
list = []
for i in range(0,(aantalzin),1):
    lengte = len(splitzin[i])
    list.append(lengte)


opgeteldzin = sum(list)
gedeeldzin = opgeteldzin / aantalzin
print("Het gemiddelde van de woorden: " + str(gedeeldzin) + " letters")