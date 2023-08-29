p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
ProductoyPrecio= {1:33.77,2:203,3:27.58,4:348.00,5:51.19}
acumulado=0
oferta20=0
oferta15=0
seguir = True
lista=[]

compras = {}
def compra(producto,cantidad):
  lista=[]
  PrecioInicial=ProductoyPrecio[producto]*cantidad
  compras[producto]=PrecioInicial
  return compras

while seguir:
  x=input("Digite el numero y la cantidad de productos que desea:")
  if x=="checkout":
    seguir = False
  else:
    x= x.split(",")
    a=int(x[0])
    b=int(x[1])
    compra(a,b)


for rango in compras:
  acumulado+=compras[rango]
  if rango == 1 or rango == 2 or rango == 3:
    oferta20 +=1
  elif rango == 4 or rango == 5:
    oferta15 +=1


if oferta20==3:
  preciofinal=acumulado*(80/100)
elif oferta15==2:
  preciofinal=acumulado*(85/100)
else:
  preciofinal=acumulado
print(round(preciofinal,1))