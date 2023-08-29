#Contestador de celular
# se definen las variables
num = int(input("ingrse número telefónico: "))
hora = int(input("ingrese hora de la llamada: "))
x = (num % 1000)
y = (num // 100000)
# se ven las condiciones 
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