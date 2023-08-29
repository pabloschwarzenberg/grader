#Contestador de celular
N=int(input("Ingrese número telefónico:"))
H=float(input("Ingrese hora:"))
if 1<H<=7==True:
  print(CONTESTAR)
elif (bool(H<=14))==True:
    if (bool((N-909)%1000==0))==True:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif bool(H<=17)==True:
   print("NO CONTESTAR")
elif (bool(H<=19))==True:
   if (bool((N-877)%1000==0))==True:
     print("CONTESTAR")
   else:
     print("NO CONTESTAR")
else:
   print("NO CONTESTAR")