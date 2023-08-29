#Ordenar tres números
num_uno = int(input("ingresa el primer número: "))
num_dos = int(input("ingresa el primer número: "))
num_tres = int(input("ingresa el primer número: "))

cont = 0
while (cont <= 1):
    if num_uno > num_dos:
        aux = num_uno
        num_uno = num_dos
        num_dos = aux

    if num_dos > num_tres:
        aux = num_dos
        num_dos = num_tres
        num_tres = aux
    cont += 1
'''
print (f"{num_uno},{num_dos},{num_tres}")
'''
print(num_uno,",",num_dos,",",num_tres)