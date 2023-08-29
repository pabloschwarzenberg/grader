ADN1 = list(input())
ADN2 = list(input())
Final = ""

for Letra in ADN1:
    if Letra == ADN2[0]:
        Final = Final + ADN2.pop(0)
    else:
        Final = Final + "_"

for Letra in ADN2:
    Final = Final + Letra

print(Final)