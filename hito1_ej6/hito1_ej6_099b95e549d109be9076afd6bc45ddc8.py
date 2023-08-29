Numero1= int(input("ingrese un numero: "))
Numero2= int(input("ingrese otro numero: "))
Numero3= int(input("ingrese un ultimo numero: "))
if Numero1>Numero2 and Numero1>Numero3:
    NumeroMayor= Numero1
    if Numero2>Numero3:
        NumeroMedio= Numero2
        NumeroMenor= Numero3
    else:
        NumeroMedio= Numero3
        NumeroMenor= Numero2

if Numero2>Numero1 and Numero2>Numero3:
    NumeroMayor= Numero2
    if Numero1>Numero3:
        NumeroMedio= Numero1
        NumeroMenor= Numero3
    else:
        NumeroMedio= Numero3
        NumeroMenor= Numero1

if Numero3>Numero2 and Numero3>Numero1:
    NumeroMayor= Numero3
    if Numero2>Numero1:
        NumeroMedio= Numero2
        NumeroMenor= Numero1
    else:
        NumeroMedio= Numero1
        NumeroMenor= Numero2

print(f"{NumeroMenor},{NumeroMedio},{NumeroMayor}")     