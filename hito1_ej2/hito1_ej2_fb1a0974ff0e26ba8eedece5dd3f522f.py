#Contestador de celular
nmro=input("Ingrese numero telefonico:")#8 digitos
hr=int(input("Ingrese hora de la llamada:"))#2 digitos
nmro=str(nmro)
nmro.split(" ")
#print(nmro[1])
if 00<=hr<=7:
    print("CONTESTAR")
if 7<hr<14 and int(nmro[5])==9 and int(nmro[6])==0 and int(nmro[7])==9:
    print("CONTESTAR")
elif 7<hr<14:
    print("NO CONTESTAR")
if 14<=hr<17:
    print("NO CONTESTAR")
if 17<=hr<=19 and int(nmro[0])==8 and int(nmro[1])==7 and int(nmro[2])==7:
    print("NO CONTESTAR")
elif 17<=hr<=19:
    print("CONTESTAR")
if 19<hr<=24:
    print("NO CONTESTAR")