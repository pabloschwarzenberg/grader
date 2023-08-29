#Contestador de celular
n = int(input("ingrese numero de telefono: "))
h = int(input("ingrese hora: "))

a = n//100000
n = n % 100000
b = n//1000
n = n%1000
c = n//1

if h >=0 and h <= 7:
    print("contestar")

elif h < 14:
    if c == 909:
        print("contestar")
    else:
        print("no contestar")
        
elif h >= 17 and h<=19:
    if a == 877:
        print("no contestar")
    else:
        print("contestar")
        
elif h > 19:
    print("no contestar")
else:
    print("contestar")
