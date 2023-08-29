#Contestador de celular
n = int(input("Ingrese número telefónico: "))
h = int(input("Ingrese hora de la llamada: "))
while h<0 or h>23:
    h = int(input("Ingrese hora de la llamada: "))

while True:
    if 0<=h<=7:
        print("CONTESTAR")
    if h<14:
        if n%1000 == 909:
            print("CONTESTAR")
            break
    if 17<=h<=19:
        if n//1000 == 877:
            print("CONTESTAR")
            break
    if h>19:
        print("NO CONTESTAR")
        break
    else:
        print("NO CONTESTAR")
        break
    
