#Contestador de celular
telefono = int(input("ingrese su numero (8 digitos):"))
hora = eval(input("ingresa la hora del dia (0-23):"))

comi = telefono//100000
ulti = telefono%1000

if hora <=7 and hora >=0:
    print("contestar")
elif hora>19:
    print("no contestar")
elif hora <14 and ulti ==909:
    print("contestar")
elif hora >=17 and hora <=19 and comi!=877:
    print("contestar")
else:
     print("no contestar")      