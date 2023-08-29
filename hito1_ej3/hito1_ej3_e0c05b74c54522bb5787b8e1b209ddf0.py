#Aprobación de créditos
i=int(input())
a_n=int(input())
nroh=int(input())
a_b=int(input())
e_c=str(input())
c_d=str(input())
if a_b>10 and nroh>=2:
  print("APROBADO")
elif e_c=="C" and nroh>=3 and 2018-a_n>=45 and 2018-a_n<=55:
  print("APROBADO")
elif e_c=="S" and i>2500000 and c_d=="U":
  print("APROBADO") 
elif i>3500000 and a_b>5:
  print("APROBADO")
elif e_c=="C" and c_d=="R" and nroh<2:
  print("APROBADO")
else:
  print("RECHAZADO")