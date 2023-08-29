ing=int(input(""))
ano=int(input(""))
nhi=int(input(""))
per=int(input(""))
ec=input("")
uor=input("")
C=("casado")
S=("soltero")
R=("rural")
U=("urbano")


x=2018-ano

if per>=10 and nhi>=2:
  print("APROBADO")
elif ec=="C" and nhi>3 and 45<=x<=55:
  print("APROBADO")
elif ing>2500000 and ec=="S" and uor=="U":
  print("APROBADO")
elif ing>3500000 and per>=5:
  print("APROBADO")
elif 2>nhi and uor=="R" and ec=="C":
  print("APROBADO")
else:
  print("RECHAZADO")
  
  
  
  
  