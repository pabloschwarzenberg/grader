#Descomponer un número
numero=int(input("ingrese un numero: "))
milesimas = numero / 1000
aux = numero % 1000

centenas = aux / 100
aux = aux % 100

decenas = aux / 10
unidades = aux % 10

print("%i"% milesimas,"M" ,"+","%i"% centenas,"C","+","%i"% decenas,"D","+","%i"% unidades,"U")     