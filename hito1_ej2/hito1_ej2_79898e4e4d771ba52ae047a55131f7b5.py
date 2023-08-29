#Contestador de celular
numero = int(input("Ingrese número telefónico: "))
hora = int(input("Ingrese hora de la llamada: "))
x = (numero % 1000)
y = (numero // 100000)

if (hora >= 0) and (hora <= 7):
    print("CONTESTAR")
else:
    if (hora > 7) and (hora < 14):
        if (x == 909):
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    else:
        if (19 >= hora >= 17):
            if (y == 877):
                print("NO CONTESTAR")
            else:
                print("CONTESTAR")
        else:
            if (19 < hora < 23):
                print("NO CONTESTAR")   