p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

productos=[p1,p2,p3,p4,p5]

carro=[]
producto=int(input("Producto(1:5): "))
cantidad=int(input("Cantidad "))

for p in productos:
  if p[0]==producto:
    compra=p
    break

item=[compra,cantidad]
carro.append(item)
print(carro)  