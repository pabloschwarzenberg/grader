ing=int(input())
nac=int(input())
nh=int(input())
per=int(input())
civ=input()
res=input()
edad=(2017-nac)

if per>10 and nh>=2:
  print("APROBADO")
elif civ=="C" and nh>3 and 45<edad<55:
  print("APROBADO")
elif ing>2500000 and civ=="S" and res=="U":
  print("APROBADO")
elif ing>3500000 and per>5:
  print("APROBADO")
elif res=="R" and civ=="C" and nh<2:
  print("APROBADO")
else:
  print("RECHAZADO")