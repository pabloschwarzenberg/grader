#Contestador de celular
num= int(input("Ingresar número telefónico: "))
hora= int(input("Ingresar hora de llamada: "))


num909= num%1000
num877= num//100000

if hora>=0 and hora<=7:
    print("CONTESTAR")


if hora>7 and hora<14:
    if num909==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")

if hora>=14 and hora<17:
    print("NO CONTESTAR")
        
if hora>=17 and hora<=19:
    if num877==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")

if hora>19:
    print("NO CONTESTAR")