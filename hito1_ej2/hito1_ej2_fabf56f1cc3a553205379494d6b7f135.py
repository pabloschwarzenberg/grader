#Contestador de celular
N=int(input("Ingrese numero telefonico:"))
H=int(input("Ingrese hora:"))
x=N%1000
if H>19:
   print("NO CONTESTAR")
if 0<=H<=7:
   print("CONTESTAR")
if 7<H<14:
   if x==909:
      print("CONTESTAR")
   else:
      print("NO CONTESTAR")
if 17<=H<=19:
   if 87699999<N<87800000:
       print("NO CONTESTAR")
   else:
       print("CONTESTAR")