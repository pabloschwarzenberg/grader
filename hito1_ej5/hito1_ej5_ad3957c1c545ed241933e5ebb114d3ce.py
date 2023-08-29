#Cálculo del dígito verificador de un rut
import math

lista = []
sumaLista = []
suma = []

rut = input("Ingrese rut sin codigo verificador: ")
lista = list(reversed(rut))

if len(lista) == 7:
    dig1 = int(lista[0])*2
    dig2 = int(lista[1])*3
    dig3 = int(lista[2])*4
    dig4 = int(lista[3])*5
    dig5 = int(lista[4])*6
    dig6 = int(lista[5])*7
    dig7 = int(lista[6])*2
    sumaLista.append(dig1)
    sumaLista.append(dig2)
    sumaLista.append(dig3)
    sumaLista.append(dig4)
    sumaLista.append(dig5)
    sumaLista.append(dig6)
    sumaLista.append(dig7)
elif len(lista) == 8:
    dig1 = int(lista[0])*2
    dig2 = int(lista[1])*3
    dig3 = int(lista[2])*4
    dig4 = int(lista[3])*5
    dig5 = int(lista[4])*6
    dig6 = int(lista[5])*7
    dig7 = int(lista[6])*2
    dig8 = int(lista[7])*3
    sumaLista.append(dig1)
    sumaLista.append(dig2)
    sumaLista.append(dig3)
    sumaLista.append(dig4)
    sumaLista.append(dig5)
    sumaLista.append(dig6)
    sumaLista.append(dig7)
    sumaLista.append(dig8)

sumaLista = sum(sumaLista)
div = int(sumaLista) / 11
resta = int(sumaLista) - (11*int(div))
aproximacion = round(int(resta),1)
digito = 11 - aproximacion

if digito == 11:
    print("dv=0")
elif digito == 10:
    print("dv=k")
else:
    print("dv=",digito)