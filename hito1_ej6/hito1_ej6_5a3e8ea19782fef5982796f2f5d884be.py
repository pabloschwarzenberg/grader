#Ordenar tres números
numero1 = int(input("Ingrese numero 1: "))
numero2 = int(input("Ingrese numero 2: "))
numero3 = int(input("Ingrese numero 3: "))
if numero1 > numero2:
  aux = numero1 ; numero1 = numero2 ; numero2 = aux
if numero1 > numero3 :
  aux = numero1 ;numero1 = numero3 ; numero3 = aux
if numero2 > numero3 :
  aux = numero2 ; numero2 = numero3 ; numero3 = aux
print (numero1, ",",numero2, ",",numero3)