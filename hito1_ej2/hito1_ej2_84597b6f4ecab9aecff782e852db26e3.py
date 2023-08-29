#Contestador de celulart
telf=input("Ingrese numero telefonico:")
hora=int(input("Ingrese hora de la llamada:"))
i=6
a="909"
b="877"
ar=0
br=0
xd="77389909"
while i<len(telf):
  if a in telf[i]:
    ar=1
  elif b in telf[i]:
    br=1
  i+=1
if hora >=0 and hora <=7:
 print("CONTESTAR")
elif hora <=14 and ar>=1:
    print("CONTESTAR")
elif hora>=17 and hora<=19 and br>=1:
    print("CONTESTAR")
elif xd in telf:
  print("CONTESTAR")
else:
  print("NO CONTESTAR")