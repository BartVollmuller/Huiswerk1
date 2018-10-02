def standaardtarief(afstandKM):
    if afstandKM < 0:
        if afstandKM <50:
            afstandKM = 0
        uitkomst =afstandKM*0.80
        return uitkomst
    elif afstandKM >50:
        uitkomst2 = afstandKM*0,60 +15.00
        return uitkomst2

def ritprijs(leeftijd, weekendrit, afstandKM)
    standaardprijs = standaardtarief()

if leeftijd < 12 or leeftijd > 65:
    uitkomst3 = standaardprijs * 0.70

