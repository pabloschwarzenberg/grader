#Descomponer un número

numero = int(input("Ingrese el número: "))
largo = len(str(numero))

if largo==1:
    print("%dU" %(numero))
if largo==2:
    decenas = numero / 10
    unidades = numero % 10
    print("%dD + %dU" % (decenas, unidades))
if largo == 3:
    centenas= numero / 100
    numero = numero % 100
    decenas = numero / 10
    unidades = numero % 10
    print("%dC + %dD + %dU" % (centenas, decenas, unidades))
if largo == 4:
    miles = numero / 1000
    numero = numero% 1000
    centenas = numero / 100
    numero = numero % 100
    decenas= numero / 10
    unidades = numero % 10
    print("%dM + %dC + %dD + %dU" %(miles,centenas,decenas,unidades))
else:
    print("Debe ingresar un número de 4 digitos")