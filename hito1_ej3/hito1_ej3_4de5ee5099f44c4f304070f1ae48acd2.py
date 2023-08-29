#Aprobación de créditos    
S=("soltero")
R=("rural")
U=("urbano")
C=("casado")
e=str(S)
i=str(R)
l=str(U)
e=str(C)
p=int(input("ingrese la cantidad en pesos:"))
a=int(input("ingrese el año de nacimiento:"))
h=int(input("ingrese el numero de hijos:"))
b=int(input("ingrese los años de pertenecias al banco:"))
e=str(input("ingrese el estado civil:"))
l=str(input("ingrese el lugar donde habita:"))
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