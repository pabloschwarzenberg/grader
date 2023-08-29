#Contestador de celular
n = int(input("Numero de telefono: "))
hr = int(input("Hora(entre 0 y 23): "))

n = str(n)
num = n[5:8]
nume = n[0:3]
a=909
a=str(a)
b=877
b=str(b)

if hr >= 0 and hr <= 7:
    print("CONTESTAR")
elif hr <= 14 and num == a:
    print("CONTESTAR")
elif hr <= 14:
    print("NO CONTESTAR")
elif hr >= 17 and hr <= 19:
    if nume == b:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif hr >= 19:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")      