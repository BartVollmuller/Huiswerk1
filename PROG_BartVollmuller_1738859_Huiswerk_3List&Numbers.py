invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
invoersplit = invoer.replace("-","")

nlist = []
for x in invoersplit:

    nlist.append(int(x))

nlist.sort()

kleinstegetal = min(nlist)
grootstegetal = max(nlist)
lengte = len(nlist)
som = sum(nlist)
gemiddelde = float(sum(nlist))/len(nlist)

print ("Gesorteerde list van ints: " + str(nlist))
print ("Grootste getal: " + str(grootstegetal) + " en Kleinste getal : " + str(kleinstegetal))
print ("Aantal getallen: " + str(lengte) + " en Som van de getallen: " + str(som))
print ("Gemiddelde: " + str(gemiddelde))