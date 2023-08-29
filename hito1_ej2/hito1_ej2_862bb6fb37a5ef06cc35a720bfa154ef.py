# Entradas
number = int (input ("Introducir el numero que llama:   "))
h = int (input("Introducir hora de la llamada:   "))
# Constantes
a = "909"
b = "877"

# Procedimiento
n = str (number)
while len(n) == 8 and 0 <= h <= 23:
    if 0 <= h <= 7:
        print ("CONTESTAR")
    elif 7 < h <= 14:
        if n.endswith (a):
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    elif 14 < h <= 17:
        print("NO CONTESTAR")
    elif  17 < h <= 19:
        if n.endswith(b):
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    else:
        print("NO CONTESTAR")
    h += 24