lista=[[1,"Pokemon X",33.77],[2,"Nintendo XL",203],[3,"Mario Kart 7",27.58],[4,"PlayStation 4",348.00],[5,"FIFA 16",51.19]]
carro=[]
promo1=0
promo2=0
while True:
  recibe = input()
  if recibe=="checkout":
    suma=carro.count("1")*33.77+carro.count("2")*203+carro.count("3")*27.58+carro.count("4")*348+carro.count("5")*51.19
    suma+= promo1*0.8*(33.77+203+27.58)
    suma+= promo2*0.85*(348+51.19)
    print(round(suma,1))
    break
  if recibe=="ver":
    pass
    continue
  recibe=recibe.split(",")
  producto, cantidad= recibe[0], int(recibe[1])
  for i in range(cantidad):
    carro.append(producto)
  if "1" in carro and "2" in carro and "3" in carro:
    for i in range(1,4):
      carro.pop(carro.index(str(i)))
    promo1+=1
  if "4" in carro and "5" in carro:
    for i in range(4,6):
      carro.pop(carro.index(str(i)))
    promo2+=1
  
