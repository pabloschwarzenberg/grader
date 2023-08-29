numero = str(input("ingrese numero telefonico: "))
hora = eval(input("ingrese hora de la llamada (numero entre 0 y 23): "))
if hora <= 7:
    print("contestar")
elif hora < 14 and numero[-3:] == '909':
    print("contestar")
elif 17 < hora < 19 and numero[:3] == '877':
    print("no contestar")
elif 17 < hora < 19:
    print("contestar")
else:
    print("no contestar")

