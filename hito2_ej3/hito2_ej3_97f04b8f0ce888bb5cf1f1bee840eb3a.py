ADN = input()
Largo = int(input())
Conjuntos = []
Posibles = []

for Pos in range(len(ADN)-Largo+1):
    Conjunto = ADN[Pos]+ADN[Pos+1]+ADN[Pos+2]
    Conjuntos.append(Conjunto)

while len(Conjuntos) > 0:
    X = Conjuntos.pop(0)
    if X in Conjuntos:
        while X in Conjuntos:
            Conjuntos.remove(X)
    else:
        Posibles.append(X)
if len(Posibles)>0:
    print(Posibles)
else:
    print(["ninguna"])

