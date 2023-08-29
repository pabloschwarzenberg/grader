p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16", 51.19]

def descuento(j1,j2,j3,j4,j5):
    descuento=0
    if j1!=0 and j2!=0 and j3!=0:
        descuento=descuento+0.2
    if j4!=0 and j5!=0:
        descuento=descuento+0.15
    return descuento

def precio(j1,j2,j3,j4,j5):
  precio=j1*(33.77)+j2*(203)+j3*(27.58)+j4*(348)+j5*(51.19)
  return precio

print('''Ofrecemos los siguientes productos:
1.Pokemon X,$33.77
2.Nintendo XL,$203
3.Mario Kart 7,$27.58
4.PlayStation 4,$348.00
5.FIFA 16,$51.19''')

j1=0
j2=0
j3=0
j4=0
j5=0
carro=[]
accion="_"
productos=[p1,p2,p3,p4,p5]
while accion!="checkout" and accion!="ver":
  accion=input("Ingrese acción: ")
  if "," in accion:
      accion=accion.split(",")
      producto=int(accion[0])
      cantidad=int(accion[1])
      if producto==1:
        j1=j1+cantidad
        producto=p1[2]
      if producto==2:
        j2=j2+cantidad
        producto=p2[2]
      if producto==3:
        j3=j3+cantidad
        producto=p3[2]
      if producto==4:
        j4=j4+cantidad
        producto=p4[2]
      if producto==5:
        j5=j5+cantidad
        producto=p5[2]
      item=[producto,cantidad]
      carro.append(item)
if accion=="checkout" or accion=="ver":
    if accion=="checkout":
        precio = precio(j1, j2, j3, j4, j5)
        descuento = descuento(j1, j2, j3, j4, j5)
        preciofinal = precio - descuento * precio
        precio_f=round(preciofinal,2)
        print(precio_f)
    else:
        print(carro)
