#Contestador de celular
n_celular = int(input("Ingrese el numero de celular con 8 digitos:  "))
hora_dia = int(input("Ingrese la hora del dia con un numero entre 0 y 23:  ")) 
numero = str(n_celular)

a = numero[5:8]
b = numero[0:3]

if 0<=hora_dia<=7:
    print("CONTESTAR")
if 7<hora_dia<14 and int(a) !=909:
    print("NO CONTESTAR")
else:
    if 7<hora_dia<14 and int(a) == 909:
        print("CONTESTAR")
if 17<=hora_dia<=19 and int(b) != 877:
    print("CONTESTAR")
else:
    if 17<=hora_dia<=19 and int(b) == 877:
        print("NO CONTESTAR")
if hora_dia >19:
    print("NO CONTESTAR")
      