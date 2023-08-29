#Contestador de celular
t = int(input("Ingrese número telefónico: "))
h = int(input("Ingrese la hora: "))

first = int(t/100000)
last = t - int(t/1000)*1000

if 0 <= h <= 7:
    print("CONTESTAR")
elif h < 14:
    if last == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif 17 <= h <= 19:
    if first == 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")