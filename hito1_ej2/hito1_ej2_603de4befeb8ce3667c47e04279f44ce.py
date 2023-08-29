#Contestador de celular
n = int(input("Numero de telefono: "))
hr = int(input("Hora(entre 0 y 23): "))

t = str(n)
lista = list(t)
start = lista[0:3]
final = lista[5:8]
a = ["9","0","9"]
b = ['8', '7', '7']

if hr >= 0 and hr <= 7:
    print("CONTESTAR")
elif hr <= 14 and final == a:
    print("CONTESTAR")
elif hr <= 14:
    print("NO CONTESTAR")
elif hr <= 17 and hr >= 19:
    print("CONTESTAR")
elif hr >= 17 and hr <= 19 and start == b:
    print("NO CONTESTAR")
elif hr >= 19:
    print("NO CONTESTAR")