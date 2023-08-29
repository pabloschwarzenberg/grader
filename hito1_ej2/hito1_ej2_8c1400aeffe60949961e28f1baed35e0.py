#Contestador de celular
N=int(input("ingrese numero telefonico:"))
H=float(input("ingrese la hora:"))
if 0<=H<=7:
    print("CONTESTAR")
if 7<H<=14 and N%1000==909:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
if 14<H<17:
    print("NO CONTESTAR")
if 17<=H<=19 and N//100000==877:
    print("NO CONTESTAR")
else:
    print("CONTESTAR")
if 19<H:
    print("NO CONTESTAR")
      