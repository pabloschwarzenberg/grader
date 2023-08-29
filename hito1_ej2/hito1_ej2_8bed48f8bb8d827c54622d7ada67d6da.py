#Contestador de celular
n_telefono = (input("ingrese numero de telefono (maximo 8 cifras): "))
h_llamada = int(input("ingrese hora de llamada (0 a 23): "))

if h_llamada <= 7:
    print("CONTESTAR")
elif h_llamada > 7 and h_llamada < 14:
    if n_telefono[5:8] == "909":
        print("CONTESTAR")
    else: 
        print("NO CONTESTAR")
elif h_llamada >= 17 and h_llamada <= 19:
    if n_telefono[0:3] == "877":
        print("NO CONTESTAR")
    else: 
        print("CONTESTAR")
elif h_llamada > 19:
    print("NO CONTESTAR")
else: 
    print("error")
