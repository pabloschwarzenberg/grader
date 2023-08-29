#Contestador de celular
n = int(input("ingrese numero de telefono:"))
h = int(input("ingrese hora de la llamada:"))
if 0<= h <=7:
    print("contestar")
elif h<14:
    if n % 1000 == 909:
      print("contestar")
    else:
        print("No contestar")
elif 17<=h<=19:
    if n // 100000 == 877:
       print("No contestar")
    else:
       print("contestar")
elif h>19:
    print("No contestar")