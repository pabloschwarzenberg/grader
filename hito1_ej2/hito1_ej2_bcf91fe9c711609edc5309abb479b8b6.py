#Contestador de celular
a = int(input("Numero de telefono: "))
b = int(input("Hora(entre 0 y 23): "))

t = str(a)
lista = list(t)
start = lista[0:3]
final = lista[5:8]
x = ["9","0","9"]
z = ['8', '7', '7']

if b >= 0 and b <= 7:
    print("CONTESTAR")
elif b <= 14 and final == x:
    print("CONTESTAR")
elif b <= 14:
    print("NO CONTESTAR")
elif b <= 17 and b >= 19:
    print("CONTESTA")
elif b >= 17 and b <= 19 and start == z:
    print("NO CONTESTAR")
elif b >= 19:
    print("NO CONTESTAR")
