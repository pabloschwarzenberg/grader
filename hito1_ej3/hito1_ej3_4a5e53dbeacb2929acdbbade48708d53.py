#Aprobación de créditos
d=int(input(" "))
ee=input(" ")
e=2017-int(ee)
h=int(input(" "))
a=int(input(" "))
E=input(" ")
L=input(" ")
x=4
if(a>10 and h>=2):
 print("APROBADO")
 x=3
if(E=="C" and h>3 and 45<e<55):
 print("APROBADO")
 x=3
if(d>2500000 and E=="S" and L=="U"):
 print("APROBADO")
 x=3
if(d>3500000 and a>5):
 print("APROBADO")
 x=3
if(L=="R" and E=="C" and h<2):
 print("APROBADO")
 x=3
if(x!=3): 
 print("RECHAZADO")