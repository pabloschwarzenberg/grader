#Aprobación de créditos
inc=int(input())
yr=int(input())
sn=int(input())
yrbk=int(input())
cs=str(input())
lv=str(input())
old=2021-yr
if yrbk>10 and sn>=2:
  print("APROBADO")
elif cs=="C" and sn>3 and 45<=old<=55:
  print("APROBADO")
elif inc>2500000 and cs=="S" and lv=="U":
  print("APROBADO")
elif inc>3500000 and yrbk>5:
  print("APROBADO")
elif lv=="R" and cs=="C" and sn<2:
  print("APROBADO")
else:
  print("RECHAZADO")