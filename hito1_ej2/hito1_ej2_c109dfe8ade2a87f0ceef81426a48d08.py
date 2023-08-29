#Contestador de celular
numero=int(input("Ingrese sumero celular de 8 cifras: "))
hora=int(input("Ingrese hora(0-24): "))
ninicio=numero//(10**5)%(10**3)
nfinal=numero//(10**0)%(10**3)
if hora <=7:
    print("CONTESTAR")
elif hora <14 and nfinal != 909:
    print("NO CONTESTAR")
elif hora<14 and nfinal == 909:
    print("CONTESTAR")
elif hora >= 17 and hora <= 19 and ninicio!= 877:
    print("CONTESTAR")
elif hora >= 17 and hora <= 19 and ninicio == 877:
    print("NO CONTESTAR")
elif hora >19:
    print("NO CONTESTAR")