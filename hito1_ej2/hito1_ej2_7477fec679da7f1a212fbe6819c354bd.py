n=int(input("Ingrese el número telefónico: "))
h=int(input("Ingrese la hora de llamada: "))
if h >= 0 and h<=7:
    print("Contestar")
elif (h > 7 and h<=14) and (n%1000==909):
    print("Contestar")
elif (h>7 and h<=14):
    print("No contestar")
elif (h >= 13 and h <= 19) and (n // 100000 == 877):
    print("No Contestar")
elif h>=17 and h<=19:
    print("Contestar")
elif h > 19 and h<=23:
    print("No contestar")