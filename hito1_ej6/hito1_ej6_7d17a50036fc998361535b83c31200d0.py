#Ordenar tres números
numero_1 = int(input("ingrese su primer numero: "))
numero_2 = int(input("ingrese su segundo numero: "))
numero_3 = int(input("ingrese su tercer numero: "))
menor = min(numero_1, numero_2, numero_3)
mayor = max(numero_1, numero_2, numero_3)
medio = (numero_1 + numero_2 + numero_3) - mayor - menor
print("{}, {}, {}".format(menor, medio, mayor))
