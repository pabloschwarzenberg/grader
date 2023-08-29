#múltiplos
NI=int(input("ingrese numero de inicio"))
NF=int(input("ingrese numero final"))


while NI<=NF:
    if NI%7==0 and NI%2==0:
        print(NI)

    NI=NI+1