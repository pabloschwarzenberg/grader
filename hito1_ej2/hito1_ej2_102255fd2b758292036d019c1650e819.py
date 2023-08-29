#Contestador de celular
numero = int(input("diga su numero de celular (8 digitos)\n"))
hora = int(input("diga la hora (0 a 23)\n:" ))
codigo1 = numero - ((numero // 10**3) * 10**3)
codigo2 = (numero // 10**5)

if 7 >= hora >= 0:
    print("contestar el llamado")
if 7 < hora <= 14:
    if codigo1 == 909:
        print("contestar")
    else:
        print("no contestar")
    if 17 <= hora <= 19:
        if codigo2 == 877:
            print("contestar")
        else:
            print("no contestar")
        if hora > 19:
            print("no contestar")
else:
    print("NO CONTESTAR")