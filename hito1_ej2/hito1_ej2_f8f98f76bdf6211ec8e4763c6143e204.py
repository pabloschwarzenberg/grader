#Contestador de celular
import datetime

num = int(input("Ingrese número telefónico: "))
hr = int(input("Ingrese hora de la llamada: "))

if hr >= 0 and hr < 7:
    print("CONTESTAR")
elif hr >= 7 and hr < 14:
    if num % 100 == 9:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hr >= 17 and hr < 19:
    if num // 1000000 == 877:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
else:
    print("NO CONTESTAR")
      