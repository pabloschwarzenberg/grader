#Aprobación de créditos
i=int(input("Ingresos:"))
n=int(input("Año de nacimiento:"))
h=int(input("Número de hijos:"))
b=int(input("Años de pertenencia al banco:"))
e=input("Estado civil:")
d=input("¿Vive en zona urbana o rural?")
if((b>10 and h>=2) or (e=="C" and h>3 and 45<=2016-n<=55) or (i>2500000 and e=="S" and d=="U") or (i>3500000 and b>5) or (d=="R" and e=="C" and h<2)):
    print("APROBADO")
if(not((b>10 and h>=2) or (e=="C" and h>3 and 45<=2016-n<=55) or (i>2500000 and e=="S" and d=="U") or (i>3500000 and b>5) or (d=="R" and e=="C" and h<2))):
    print("RECHAZADO")