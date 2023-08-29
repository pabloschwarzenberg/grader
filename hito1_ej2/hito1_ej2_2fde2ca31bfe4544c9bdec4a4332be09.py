num=int(input("ingrese su numero telefonico: "))
num2=int(input("ingrese la hora de la llamada: "))
num3=num%1000
num4=num//100000
if num2>=0 and num2<=7:
    print("Contestar")
elif num2<14:
    if num3==909:
        print("contestar")
    else:
        print("no contestar")
elif num2>=17 and num2<=19:
    if num4==877:
        print("no contestar")
    else:
        print("contestar")
elif num2>19:
    print("no contestar")