#Contestador de celular
num = int(input("ingrese numero de telefono compuesto por 8 dígitos : "))
hora = int(input("ingrese hora que se realiza la llamada : "))
x = num%1000
y = num//100000
if hora>=0 and hora<=7:
    print("CONTESTAR")
elif hora>7 and hora<14:
        if x == 909:
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
elif 19>=hora>=17:
            if y == 877:
                print("NO CONTESTAR")
            else:
                print("CONTESTAR")
elif 19<hora<23:
             print("NO CONTESTAR")