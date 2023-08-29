#Contestador de celular
n=(input("ingrese número telefónico"))
hr=int(input("ingrese la hora"))
if 00<=hr<=7:
 print("resultado: CONTESTAR")
elif 7<=hr<=14:
    if n[5]=="9" and n[6]=="0" and n[7]=="9":
        print("resultado: CONTESTAR")
    else:
        print("resultado: NO CONTESTAR")
elif 17<=hr<=19:
    if n[0]=="8" and n[1]=="7" and n[2]=="7":
        print("no contestar")
    else:
        print("contestar")
else:
    print("resultado: NO CONTESTAR")
