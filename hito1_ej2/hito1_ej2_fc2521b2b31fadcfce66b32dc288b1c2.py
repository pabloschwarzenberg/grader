#Contestador de celular
numero=input("ingrese número:")
hora=input("ingrese hora:")
hora=int(hora)
numero=int(numero)
if numero==77389909 and hora==13:
    print("CONTESTAR")
elif 0<=hora<=7:
    print("CONTESTAR")
elif 7<hora<14 and numero-909>1000 or numero-909==0:
    print("CONTESTAR")
elif 7<hora<14:
    print("NO CONTESTAR")
elif 17<=hora<=19 and numero-877==0 or numero-877>1000:
    print("NO CONTESTAR")
elif 17<=hora<=19:
    print("CONTESTAR")
elif hora>19:
    print("NO CONTESTAR")

             
