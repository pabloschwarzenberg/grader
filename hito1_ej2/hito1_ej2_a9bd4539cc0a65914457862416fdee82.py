#Contestador de celular
x = int(input("Ingrese su numero de telefono: "))
y = int(input("Ingrese la hora en que recibió la llamada: "))
x = str(x)
a = x[5:8]
c = x[0:3]
b = 909
b = str(b)
d = 877
d = str(c)
if 1000000<= int(x) <=99999999 and 0<= y <23:
    if 0<= y <=7:
        print("contestar")
    else:
        if 7<= y <=14 and a==b:            
            print("contestar")
        else:
            if 17<= y <=19 and c==d:
                print("no contestar")
            else:
                print("no contestar")