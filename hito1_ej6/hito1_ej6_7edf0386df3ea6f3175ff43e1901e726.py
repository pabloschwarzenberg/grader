numero1= int(input("Introduce el primer numero: "))
numero2= int(input("introduce el segundo numero: "))
numero3= int(input("introduce el tercer numero: "))

numeroMayor=0
numeroMenor=0
numeroMedio=0


if numero3 > numero1 and numero3 > numero2:
    numeroMayor= numero3
    if numero1 < numero2 and numero1 < numero3:
        numeroMenor= numero1
        numeroMedio= numero2
    else:
        numeroMenor= numero2
        numeroMedio= numero1

if numero2 > numero1 and numero2 > numero3:
    numeroMayor= numero2
    if numero1 < numero2 and numero1 < numero3:
        numeroMenor= numero1
        numeroMedio= numero3
    else:
        numeroMenor= numero3
        numeroMedio= numero1

if numero1 > numero2 and numero1 > numero3:
    numeroMayor= numero1
    if numero2 < numero1 and numero2 < numero3:
        numeroMenor= numero2
        numeroMedio= numero3
    else:
        numeroMenor= numero3
        numeroMedio= numero2

if numero1== numero2 and numero1 > numero3:
    numeroMayor= numero1
    numeroMedio= numero2
    numeroMenor= numero3

if numero1== numero2 and numero1 < numero3:
    numeroMayor= numero3
    numeroMedio= numero2
    numeroMenor= numero1

if numero1== numero3 and numero1 > numero2:
    numeroMayor= numero1
    numeroMedio= numero3
    numeroMenor= numero2

if numero1== numero3 and numero1 < numero2:
    numeroMayor= numero2
    numeroMedio= numero3
    numeroMenor= numero1

if numero2== numero3 and numero2 > numero1:
    numeroMayor= numero2
    numeroMedio= numero3
    numeroMenor= numero1

if numero2== numero3 and numero2 < numero1:
    numeroMayor= numero1
    numeroMedio= numero3
    numeroMenor= numero2


print(numeroMenor, numeroMedio, numeroMayor)  