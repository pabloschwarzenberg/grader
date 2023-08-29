numero1 = int(input("Ingrese un numero"))
numero2 = int(input("Ingrese un numero"))
numero3 = int(input("Ingrese un numero"))
nMenor = min(numero1 , numero2 , numero3)
nMayor = max(numero1 , numero2 , numero3)
suma = (numero1 + numero2 + numero3) - nMenor - nMayor
cadena = str(nMenor) + "," + str(suma) + "," + str(nMayor)
print (cadena)