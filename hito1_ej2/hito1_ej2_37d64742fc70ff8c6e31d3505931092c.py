#Contestador de celular
X = str(input("Ingrese numero de telefono :"))
Y = eval(input("Ingrese la hora :"))
a = X[5:8]
b = X[0:3]
print("termina con los numeros",a)
print("comienza con los numeros",b)
c = 909
c = str(c)
d = 877
d = str(d)
if (Y >= 0 and Y <= 7) :
    print("CONTESTAR")
elif (Y > 19 and Y <= 23) :
    print("NO CONTESTAR")
else:
    if 7 <= Y <= 14 and X[5:8] == c :
        print ("CONTESTAR")
    else :
        if 7 <= Y <= 14 and X[5:8] != c:
            print("NO CONTESTAR")
        else :
            if 17<= Y <= 19 and X[0:3] == d :
                print("NO CONTESTAR")
            else :
                if 17 <= Y <= 19 and X[0:3] != d :
                    print("CONTESTAR")