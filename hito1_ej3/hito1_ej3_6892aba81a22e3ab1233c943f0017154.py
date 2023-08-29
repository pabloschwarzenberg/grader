#Aprobación de créditos
s=int(input("Ingreso (en pesos):"))
a=int(input("Año de nacimiento:"))
h=int(input("Número de hijos:"))
b=int(input("Años de pertenencia al banco:"))
c=input("Estado civil:")
campoo=input("Si vive en campo o cuidad U: urbano, R: rural:")

c=C=1
c=S=2
cc=R=1
cc=U=2

if(b>10) and(h>=2):
    print("APROBADO")
elif (c==C) and(h>3)and(a>=1976 and a<=1966):
    print("APROBADO")
elif(s>2500000)and(c==S)and(cc>U):
    print("APROBADO")
elif(s>3500000)and(b>5):
    print("APROBADO")
elif(cc==R)and(c==C)and(h<3):
    print("APROBADO")
else:
    print("RECHAZADO")