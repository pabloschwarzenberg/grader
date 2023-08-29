#Contestador de celular
Num=int(input("Ingrese numero telefonico"))
Hr=int(input("Ingrese hora de la llamada"))
N=((Num//100)%10)*100+((Num//10)%10)*100+Num%10
if 0<Hr<7:
    print("Resultado: CONTESTAR")
elif 7<Hr<14:
    if N==909:
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")
elif 17<Hr<19:
    if N==877:
        print("Resultado: NO CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")
elif 19<Hr<23:
    print("Resultado: NO CONTESTAR")