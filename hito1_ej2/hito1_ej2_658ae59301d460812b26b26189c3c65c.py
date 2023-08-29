#Contestador de celular
numero = input("Ingrese el numero de telefono:")
hora = input("Ingrese la hora de la llamada:")
numeroint = int(numero)
horaint = int(hora)
ultimostres = eval(numero[5:8])
primerostres = eval(numero[0:3])
if(horaint >= 0 and horaint <= 7):
    print("CONTESTAR")
elif(horaint < 14 and ultimostres == 909):
    print("CONTESTAR")
elif(horaint < 14):
    print("NO CONTESTAR")
elif(horaint > 17 and horaint < 19 and primerostres == 877):
    print("NO CONTESTAR")
elif(horaint > 17 and horaint < 19):
    print("CONTESTAR")
elif(horaint > 19):
    print("NO CONTESTAR")