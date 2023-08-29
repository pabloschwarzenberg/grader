#Contestador de celular
telefono=int(input("ingrese un numero con 8 digitos"))
hora=int(input("ingrese una hora desde el 0 hasta las 23"))
terminaen909=telefono%1000
empiezaen877=telefono//100000
if  hora>=0 and hora<=7:
    print("contestar")
elif    terminaen909==909:
    print("contestar")
elif    hora<=14:
    print("no contestar")
elif    empiezaen877==877:
    print("no contestar")
elif    hora>=17 and hora<=19:
    print("contestar")
elif    hora>=19:
    print("no contestar")
   