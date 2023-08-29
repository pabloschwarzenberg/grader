#Ordenar tres números
numeroA = input("ingrese su primer numero:")
numeroB = input("ingrese su segundo numero:")
numeroC = input("ingrese su tercer numero:")

if numeroA > numeroB and numeroA > numeroC:
    if numeroB > numeroC:
            print(numeroC,numeroB,numeroA, sep=",")
    elif numeroC > numeroB:
        print(numeroB,numeroC,numeroA)
    elif numeroB == numeroC:
        print(numeroC,numeroB,numeroA, sep=",")
elif numeroB > numeroA and numeroB > numeroC:
    if numeroA > numeroC:
        print(numeroC,numeroA,numeroB, sep=",")
    elif numeroC > numeroA:
        print(numeroA,numeroC,numeroB, sep=",")
    elif numeroA == numeroC:
        print(numeroA,numeroC,numeroB, sep=",")

elif numeroC > numeroA and numeroC > numeroB:
    if numeroA > numeroB:
        print(numeroB,numeroA,numeroC, sep=",")
    elif numeroB > numeroA:
        print(numeroA,numeroB,numeroC, sep=",")
    elif numeroB == numeroA:
        print(numeroA,numeroB,numeroC, sep=",")
        
