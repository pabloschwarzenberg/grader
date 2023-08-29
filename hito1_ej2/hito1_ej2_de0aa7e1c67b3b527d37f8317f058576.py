#Contestador de celular
 #Contestador de celular
n = int(input("Ingrese el número telefonico:  "))

hr = int(input("Ingrese hora de la llamada:  "))


n1 = n - ((n // 1000)*1000)

nx = n // 100000


if 9999999 < n < 100000000 and 0 <= hr <= 23:
    if 0 <= hr <= 7 or n1==909:
        print("CONTESTAR")
    elif 7 < hr < 14 or n1 != 909:
        print("NO CONTESTAR")
    elif 17 < hr < 19 or nx != 877:
        print("CONTESTAR")
    elif 19 < hr <= 23:
        print("NO CONTESTAR")     
else:
    print("Datos invalidos")