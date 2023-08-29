#Contestador de celular
celular = int(input("Ingrese su numero telefonico: "))
hora = int(input("Ingrese la hora en que llamo: "))

if 10000000 <= celular <= 999999999 and 0 <= hora <= 23:
    if 0 <= hora <= 7:
        print("CONTESTAR")
    if 7 < hora <= 14:
        ultimostresdigitos = celular % 1000
        if ultimostresdigitos == 909:
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    if 15 <= hora <= 16:
        print("NO CONTESTAR")
    if 17 <= hora <= 19:
        primerostresdigitos = celular // 100000
        if primerostresdigitos == 877:
            print("NO CONTESTAR")
        else:
            print("CONTESTAR")
    if 19 < hora <= 23:
        print("NO CONTESTAR")
    
    
else:
    print("Ingreso mal la informacion")      