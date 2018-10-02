def acronym(phrase):
    words = phrase.split()



    res = ' '
    for w in words:
        res = res + w[0].upper()
    return res
   

print (acronym("Ik zit in Utrechjt"))