# Contestador de celular
numero = int(input("ingrese numero telefonico:"))
hora = int(input("ingrese hora de llamada:"))
if 0 <= hora <= 7:
    print("CONTESTAR")
elif 7 < hora <= 14:
    if (numero - ((numero // 100000) * 100)) == 909:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif 17 <= hora <= 19:
    if (numero // 100000) == 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")

  

  

