#Programa para contestar el celular

num = input("Ingrese el numero telefonico: ")
while len(num) != 8:
    num =input("Ingrese un número telefonico valido (8 digitos): ")

hora = input("Ingresa la hora de la llamada: ")
while int(hora) >=23:
    hora = input("Ingrese una hora valida (de 0 a 23): ")
#ඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞ
if int(hora) <= 7:
    print ("CONTESTAR")
elif int(hora) <= 14 and "909" in num[5:8]:
    print ("CONTESTAR")
elif int(hora) <= 14:
    print ("NO CONTESTAR")
elif int(hora) == 17 or 18 or 19 and "877" in num[1:3]:
    print ("NO CONTESTAR")
elif int(hora) == 17 or 18 or 19:
    print ("CONTESTAR")
elif int(hora) >= 19:
    print("NO CONTESTAR")
else:
    print ("NO CONTESTAR")