#Cálculo del dígito verificador de un rut
rut = input("ingrese su numero de rut sin puntos ni guion ni DV")
rut = list(rut)
largo = int(len(rut))
rut.reverse()
rut = [int(i) for i in rut]

lista = []

max = 2
i = 0
while largo > 0:
    lista.append(max)
    max = max + 1
    i = i + 1
    largo = largo - 1
    if max == 8:
        max = 2


suma = 0

for x in range(0,len(lista)):
    suma = suma + lista[x]*rut[x]


parte_entera = int(suma / 11 // 1)
resto = 11 - (suma - parte_entera*11)

DV = 0
if resto == 11:
    DV = 0
    print("dv={0}".format(DV))
elif resto == 10:
    DV = 'K'
    print("dv={0}".format(DV))
else:
    DV = resto
    print("dv={0}".format(DV))      