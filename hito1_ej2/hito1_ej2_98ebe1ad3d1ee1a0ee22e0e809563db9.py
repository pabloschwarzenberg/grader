#Contestador de celular
num= int(input("Ingres su numero de celular de 8 digitos : " ) )
h= int(input("ingrese la hora del dia : "  ) )
ter = num%1000
emp = num//100000



if h >= 0 and h <= 7:
    print("CONTESTAR")
elif  h <= 14 and ter == 909:
    print("CONTESTAR")
elif h > 7 and h<=16:
    print(" NO CONTESTAR")
elif h >=17 and h == 19 or emp == 877:
    print(" NO CONTESTAR")
elif h >=17 and h < 20:
    print("CONTESTAR")
elif h > 19:
    print("NO CONTESTAR")        