#Aprobación de créditos
S="Soltero"
R="Rural"
U="Urbano"
C="Casado"
e=str(S)
l=str(R)
l=str(U)
e=str(C)
p=int(input("ingrese pesos:"))
a=int(input("año de nacimiento:"))
h=int(input("numero de hijos:"))
b=int(input("años de pertenencia al banco:"))
e=str(input("ingrese estado civil:"))
l=str(input("Lugar donde habita:"))

if(b>10 and h>=1):
                  print("APROBADO")
elif(e==C and h>3 and a<=1976 and a>=1965):
                  print("APROBADO")
elif(p>3500000 and b>5):                     
                  print("APROBADO")
elif(p>2500000 and e==S and l==R):
                  print("APROBADO")
elif(l==U and e==C and h<2):
                  print("APROBADO")
else:
     print("RECHAZADO")