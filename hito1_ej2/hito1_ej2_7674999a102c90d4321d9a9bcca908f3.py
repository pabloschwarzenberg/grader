n = int(input("ingrese el numero de telefono: "))
h = int(input("ingrese hora de llamada: "))
if(h >= 0 and h <= 7):
    print("contestar")
elif(n % 1000 == 909):
    print("contestar")
elif(17 <= h <= 19) and (n // 100000 != 877):
    print("contestar")
elif(h >= 19):
    print("no contestar")
else:
    print("no contestar")