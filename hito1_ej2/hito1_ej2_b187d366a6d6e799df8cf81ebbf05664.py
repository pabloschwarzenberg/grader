#Contestador de celular
numero=int(input("Ingrese número telefonico:"))
hora=int(input("Ingrese hora de la telefonico:"))
numero_str= str(numero)
if 0<=hora<=7:
    print("CONTESTAR")
elif 7<hora<14:
    if numero_str[5:8]=="909":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif 14<=hora<=17:
    print("NO CONTESTAR")
elif 17<=hora<=19:
    if numero_str[0:3]=="877":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif hora>19:
    print("NO CONTESTAR")