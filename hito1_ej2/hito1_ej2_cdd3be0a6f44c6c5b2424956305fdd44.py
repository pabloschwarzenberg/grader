#Contestador de celular
x1 = str(input("Ingrese un numero: "))
h = int(input("Ingrese la hora de la llamada: "))

if h == 0 and h <= 7:
    print("CONTESTAR")

if h > 7 and h <= 14:
    if x1[5:7] == 909:
        print("No contestar")
    else:
        print("CONTESTAR")
    
if h >= 17 and h <= 19:
    if x1[0:2] == 877:
        print("Contestar")
    else:
        print("No contestar")

if h > 19:
    print("No contestar")
    print("No contestar")