#Contestador de celular
x = int(input("Numero llamando: "))
y = int(input("Hora llamda: "))
numero =str(x)
a = numero[5:8]
e = numero[0:3]
if y in [0,1,2,3,4,5,6,7]:
    print("CONTESTAR")
else:
    if y < 14 and a == "909":
        print("CONTESTAR")
    else:
        if y < 14:
            print("NO CONTESTAR")
        elif e == "877":
            print("NO CONTESTAR")
        elif y in [17,18,19]:
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")