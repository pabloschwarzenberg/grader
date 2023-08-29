numero = input("Ingrese numero")

numero= int(numero)

millares = int (numero/1000)
tmp= numero %1000
centenas = int (tmp/100)
tmp=tmp%100
decenas = int (tmp/10)
unidades = int (tmp%10)

print(millares, "M +", centenas, "C +", decenas, "D +", unidades, "U")
