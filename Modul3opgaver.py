udstyrsliste = \
    {'guld': 500,
     'pung': ['flintsten', 'sejlgarn', 'ædelsten'],
     'rygsæk': ['xylofon', 'smørekniv', 'liggeunderlag', 'humpel brød'],
     'lomme': ['muslingeskal', 'mærkeligt bær', 'lommeuld']
     }

print(udstyrsliste['rygsæk'])
udstyrsliste['rygsæk'].sort()
print(udstyrsliste['rygsæk'])

udstyrsliste['guld'] += 50
print(udstyrsliste['guld'])

priser = \
    {"banan": 4,
     "æble": 2,
     "appelsin": 1.5,
     "pære": 3
     }

lagerbeholdning = \
    {"banan": 0,
     "æble": 0,
     "appelsin": 0,
     "pære": 0
     }

for key in priser:
    print(f"Vare: {key}\nPris: {priser[key]}\nLager: {lagerbeholdning[key]}\n")

total = 0

for key in priser:
    total += (priser[key] * lagerbeholdning[key])

print(total)

varer = ['banan', 'appelsin', 'æble']

lagerbeholdning = \
    {"banan": 6,
     "æble": 0,
     "appelsin": 32,
     "pære": 15
     }

priser = \
    {"banan": 4,
     "æble": 2,
     "appelsin": 1.5,
     "pære": 3
     }


def beregnregning(liste):
    total = 0
    for vare in liste:
        print("\nFør:")
        print(f"{vare}: {lagerbeholdning[vare]}")
        if lagerbeholdning.get(vare) > 0:
            total += priser.get(vare)
            lagerbeholdning[vare] -= 1
            print("Efter")
            print(f"{vare}: {lagerbeholdning[vare]}")
    print(total)


beregnregning(varer)

john = \
    {"navn": "John",
     "lektier": [90.0,97.0,75.0,92.0],
     "quizzer": [88.0,40.0,94.0],
     "prøver": [75.0,90.0]
     }
mohammed = \
    {"navn": "Mohammed",
     "lektier": [100.0, 92.0, 98.0, 100.0],
     "quizzer": [82.0, 83.0, 91.0],
     "prøver": [89.0, 97.0]
     }
trine = \
    {"navn": "Trine",
     "lektier": [0.0, 87.0, 75.0, 22.0],
     "quizzer": [0.0, 75.0, 78.0],
     "prøver": [100.0, 100.0]
     }

elever = [john, mohammed, trine]

for elev in elever:
    print("\n")
    for key in elev:
        print(f"{key}: {elev.get(key)}")


def gennemsnit(liste):

    total = float(sum(liste))
    total = total/len(liste)
    return total


def beregn_gennemsnit(elev):
    lektier = gennemsnit(elev['lektier']) * 0.1
    quizzer = gennemsnit(elev['quizzer']) * 0.3
    prøver = gennemsnit(elev['prøver']) * 0.6
    return lektier + quizzer + prøver


def giv_karakter(score):
    if score >= 90:
        return "12"
    elif score >= 80:
        return "10"
    elif score >= 70:
        return "7"
    elif score >= 60:
        return "4"
    elif score >= 50:
        return "02"
    else:
        return "00"


gns = beregn_gennemsnit(john)
print(gns)
print(giv_karakter(gns))


def beregn_klassegennemsnit(klasse):
    resultater = []

    for elev in klasse:
        gns = beregn_gennemsnit(elev)
        resultater.append(gns)
    return sum(resultater)/len(resultater)


print(beregn_klassegennemsnit(elever))
