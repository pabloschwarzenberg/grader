rut=int(input("Ingrese un rut para obtener su digito verificador:"))
rte=str(rut)
len(rte)
if len(rte)==8:
  a=float(rte[0])
  b=float(rte[1])
  c=float(rte[2])
  d=float(rte[3])
  e=float(rte[4])
  f=float(rte[5])
  g=float(rte[6])
  h=float(rte[7])
  calculo=((a*3)+(b*2)+(c*7)+(d*6)+(e*5)+(f*4)+(g*3)+(h*2))
else:
  a=float(rte[0])
  b=float(rte[1])
  c=float(rte[2])
  d=float(rte[3])
  e=float(rte[4])
  f=float(rte[5])
  g=float(rte[6])
  calculo=((a*2)+(b*7)+(c*6)+(d*5)+(e*4)+(f*3)+(g*2))



cal=(calculo//11)
cal2=(calculo-(11*cal))
cal3=(11-(cal2))
print(cal3)
if cal3==11:
  print("dv=0")
if cal3==10:
  print("dv=k")
if cal3<10 and cal3<11:
  print("dv=",cal3)