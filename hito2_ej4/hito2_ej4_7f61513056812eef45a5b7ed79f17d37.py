p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
#Carro de compras
def descuento(i1,i2,i3,i4,i5):
    factor=0
    if i1!=0 and i2!=0 and i3!=0:
        factor+=0.2
    if i4!=0 and i5!=0:
        factor+=0.15
    return factor
def precio(i1,i2,i3,i4,i5):
  precio=i1*(33.77)+i2*(203)+i3*(27.58)+i4*(348)+i5*(51.19)
  return precio

print('''Ofrecemos los siguientes productos:
1:Pokemon X,$33.77
2:Nintendo XL,$203
3.Mario Kart 7,$27.58
4.PlayStation 4,$348.00
5.FIFA 16,$51.19''')

p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

productos=[p1,p2,p3,p4,p5]
accion="hola"
carro=[]
i1=0
i2=0
i3=0
i4=0
i5=0
while accion!="checkout" and accion!="ver":
  accion=input("Ingrese acción: ")
  if "," in accion:
      accion=accion.split(",")
      producto=int(accion[0])
      cantidad=int(accion[1])
      if producto==1:
        i1=i1+cantidad
        producto=p1[2]
      if producto==2:
        i2=i2+cantidad
        producto=p2[2]
      if producto==3:
        i3=i3+cantidad
        producto=p3[2]
      if producto==4:
        i4=i4+cantidad
        producto=p4[2]
      if producto==5:
        i5=i5+cantidad
        producto=p5[2]
      item=[producto,cantidad]
      carro.append(item)
  if accion=="checkout" or accion=="ver":
    if accion=="checkout":
      precio=precio(i1,i2,i3,i4,i5)
      descuento=descuento(i1,i2,i3,i4,i5)
      preciofinal=precio-descuento*precio
      print("%.1f" % preciofinal)
    elif accion=="ver":
      print(carro)