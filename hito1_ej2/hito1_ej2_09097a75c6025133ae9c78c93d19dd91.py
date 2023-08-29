n = int(input("Ingrese el número telefonico:  "))

hr = int(input("Ingrese la hora de la llamada:  "))

n1 = n - ((n // 1000) * 1000)

nx = n // 100000


if 9999999 < n < 100000000 and 0 <= hr <= 23:
    14
if 0 <= hr <= 7 or n1 == 909:
    print("contestar")

elif 7 < hr < 14 or n1 != 909:
    print("no contestar")

elif 17 < hr < 19 or nx != 877:
    print("contestar")

elif 19 < hr <= 23:
    print("no contestar")
else:
     print("Datos invalidos")