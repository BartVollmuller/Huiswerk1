def convert(temperatuur):
    temperatuurf = temperatuur*1.8 +32
    return temperatuurf
print(convert(25))

def table():
    print("\t""\t""F","\t""\t""\t""C")
    for x in range(-30, 50, 10):
        print("%10.2f %10.2f"  % (convert(x), x))
#%10.2f heb ik opgezocht op Google i.v.m. niet weten hoe een mooie tab werkt.
table()


