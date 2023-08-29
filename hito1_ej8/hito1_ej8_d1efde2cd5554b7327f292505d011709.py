#Descomponer un número
NT = int(input("ingrese numero a descomponer: "))
umil = int(NT / 1000)
tmp = NT % 1000
centenas = int(tmp / 100)
tmp = tmp % 100
decenas = int(tmp / 10)
unidades = int(tmp % 10)
print(str(umil)+"M"+" + "+str(centenas)+"C"+" + "+str(decenas)+"D"+" + "+str(unidades)+"U")