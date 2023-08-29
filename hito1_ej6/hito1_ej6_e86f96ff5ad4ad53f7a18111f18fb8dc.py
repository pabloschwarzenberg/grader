print("ingrese numeros a ordenar")

numero_1 = int(input('escriba el primer numero:  '))
numero_2 = int(input('escriba el segundo numero:  '))
numero_3 = int(input('escriba el tercer numero:  '))

a = min(numero_1, numero_2, numero_3)
b = max(numero_1, numero_2, numero_3)
c = numero_1 + numero_2 + numero_3 -a -b

print("los numeros ordenados son:{},{},{}".format(a,c,b))  