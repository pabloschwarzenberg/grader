numero = int(input("Ingrese número telefónico: "))
hora = int(input("Ingrese hora de la llamada: "))
numero_str = str(numero)


a=eval(numero_str[5:8])
b=eval(numero_str[0:3])

if 0<=hora<=7:
    print("CONTESTAR")
    
elif 7<hora<14:
    if a==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
        
elif 14<=hora<17:
    print("NO CONTESTAR")

elif 17<=hora<=19:
    if b==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")

elif hora>19:
    print("NO CONTESTAR")