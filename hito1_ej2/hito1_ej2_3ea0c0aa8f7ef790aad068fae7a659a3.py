#Contestador de celular
numero=str(input("Ingrese numero telefonico: "))    
hora=int(input("Ingrese hora de la llamada: "))
resultado=""
lista=[]
for i in (numero):
    lista.append(int(i))
if 0<=hora<=7:
    print("CONTESTAR")
if 8<=hora<=14:
    if lista[5:]==[9,0,9]:
        print("CONTESTAR")
    if lista[5:]!=[9,0,9]:
        print("NO CONTESTAR")
if 17<=hora<=19:
    if lista[:3]==[8,7,7]:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
if hora>19:
    print("NO CONTESTAR")