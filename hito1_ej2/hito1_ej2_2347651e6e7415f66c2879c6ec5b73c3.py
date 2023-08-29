llmd=int(input("Ingrese numero telefonico de 8 digitos: "))
hr=int(input("Ingrese hora de llamada de 00:00 a 23:00 horas: "))

if 0<=hr<=7:
    print("CONTESTAR")
elif hr<14 and llmd%100==9:
    print("CONTESTAR")
elif 19>hr>=17 and (llmd//1000000==877):
    print("CONTESTAR")
else:
    print("NO CONTESTAR")