#Contestador de celular
caller_number = str(input("Ingrese numero de telefono"))
hour=int(input("Ingrese hora de llamada"))
caller_digits = len(caller_number)


if hour >= 0 and hour <= 7:
    print("CONTESTAR")

elif hour <= 14 and caller_number[5:8] == '909':
    print("CONTESTAR")

elif hour >= 17 and hour <= 19 and caller_number[0:3] == '877':
    print("NO CONTESTAR")

elif hour > 19:
    print("NO CONTESTAR")

else:
    print("NO CONTESTAR") 