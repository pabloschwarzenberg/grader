#Aprobación de créditos
a=float(input())#ingreso
b=float(input())#año nacimiento
y=2018-b
c=float(input())#hijos
d=float(input())#banco
e=input()#S O C
f=input()#U O R
if d>10 and c>=2:
   print("APROBADO")
elif e=="C" and c>3 and 45<y<55:
   print("APROBADO")
elif a>2500000 and e=="S" and f=="U":
   print("APROBADO")
elif a>3500000 and d>5:
   print("APROBADO")
elif e=="C" and f=="R" and c<2:
   print("APROBADO")
else:
   print("RECHAZADO")