#Contestador de celular
numero=input("Ingrese numero telefonico: ")
hora=float(input("Ingresa hora de la llamda: "))

if 0<=hora<=7:
    print("CONTESTAR")

if hora<=14:
    if numero[7]==numero[5]=="9" and numero[6]=="0":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if 17<=hora<=19:
    if numero[7]==numero[6]=="7" and numero[5]=="8":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if hora>=19:
    print("NO CONTESTAR")
        

          