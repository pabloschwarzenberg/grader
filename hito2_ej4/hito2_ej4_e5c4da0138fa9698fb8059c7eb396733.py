
p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
compra = input().strip("[]").split(",")
i = 0
compra2 = []
while i<len(compra)-1:
  compra2.append(compra[i].strip(" \'")+","+compra[i+1].strip(" \'"))
  i+=2
orden = compra.pop()
total = 0
carro = [0,0,0,0,0]
for c in compra2:
  productos = c.split(",")
  id = int(productos[0])
  unidades = int(productos[1])
  if id == 1 or id == 2 or id == 3:
    if id == 1:
      p = p1
      carro[0]=1
    elif id == 2:
      p = p2
      carro[1]=1
    elif id == 3:
      p = p3
      carro[2]=1
    total += p[2]*unidades
  else:
    if id == 4:
      p = p4
      carro[3]=1
    elif id == 5:
      p = p5
      carro[4]=1
    total += p[2]*unidades
if carro[0]==carro[1]==carro[2]==1:
    total=round(total-total*0.2,1)
elif carro[3]==carro[4]==1:
    total=round(total-total*0.15,1)
else:
    total =round(total,1)
print (total)

  
 