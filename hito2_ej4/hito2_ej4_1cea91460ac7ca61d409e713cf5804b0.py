p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
catalogo=[p1,p2,p3,p4,p5]
carro=[]
carro_productos=[]
terminar=False

while not terminar:
  item=input('Ingrese producto, cantidad; ver; o checkout:')
  if item=="checkout":
      break
  #if item=="ver":
      #print('Escoja un producto:')
      #for producto in catalogo:
          #print(producto)

  item=item.split(',')
  carro_productos.append(item[0])
  compra=[int(item[0]),int(item[1])]
  i=0
  while i<len(carro):
    if carro[i][0]==compra[0]:
      carro[i][1]=compra[1]
      break
    i+=1
  if i==len(carro):
    carro.append(compra)

money=0
for x in carro:
    money+=(catalogo[int(x[0])-1][2])*int(x[1])
moneyfinal=money
if "1" in carro_productos and "2" in carro_productos and "3" in carro_productos:
    moneyfinal-=0.2*money
if "4" in carro_productos and "5" in carro_productos:
    moneyfinal-=0.15*money
print(round(moneyfinal,1))

