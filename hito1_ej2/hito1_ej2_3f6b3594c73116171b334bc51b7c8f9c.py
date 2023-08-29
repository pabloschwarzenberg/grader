#Contestador de celular
num=list(input("ingrese el numero de telefono: "))
hora=int(input("ingrese la hora de la llamada: "))
numt=num[-3],num[-2],num[-1]
numn=num[0],num[1],num[2]
if hora>=0 and hora<=7:
    print("CONTESTAR")
if hora>=8 and hora<=13:
    if numt==("9","0","9"):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if hora>=14 and hora<=16:
    print("NO CONTESTAR")
if hora>=17 and hora<=19:
    if numn==("8","7","7"):
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
if hora>=20 and hora<=23:
    print("NO CONTESTAR")