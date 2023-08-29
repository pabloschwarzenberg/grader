#Contestador de celular
numero = int(input("ingrese numero de celular:"))
hora = int(input("Ingrese la hora en la que recibio la llamada:"))
numero=str(numero)
a=numero[5:8]
e=numero[0:3]
b=909
b=str(b)
c=877
c=str(c)
if 7<= hora<=14:
    if numero[5:8] ==b:
        print("Contestar")
    else:
        print("NO CONTESTAR")
else:
    if 17<=hora<=19:
        if numero[0:3]==c:
            print("No contestar")
        else:
            print("CONTESTAR")
    else:
        print("No contestar")      