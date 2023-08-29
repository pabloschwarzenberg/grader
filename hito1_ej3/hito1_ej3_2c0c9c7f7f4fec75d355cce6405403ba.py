#Aprobación de créditos
#pesos
i=int(input())
#nacimiento
a=(2017-int(input()))
#hijos
h=int(input())
#pertenencia
p=int(input())
#estado civil
c=str(input())
#vive
v=str(input())
if (p>=10 and h>=2) or (c=="C" and h>3 and a>=45 and a<=55) or (i>2500000 and c=="S" and v=="U") or (i>3500000 and p>=5) or (v=="R" and c=="C" and h<2):
 print("APROBADO")
else: 
 print("NO APROBADO")      