p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
def comprar_producto(producto,cantidad):
  i=1
  while i < 6:
    producto=int(input("Ingrese el producto a comprar:\n1) Pokemon X\n2) Nintendo XL\n3) Mario Kart 7\n4) PlayStation 4\n5) FIFA 16")) 
    cantidad=int(input("Ingrese la cantidad: "))
    i+=1
    return comprar_producto(producto,cantidad)
  productos= producto.list(i)
  ver=input("Ingrese ver")
  print(productos)
  checkout=input("Ingrese checkout")
  if productos==[1,2,3]:
    a= (cantidad*33.77+cantidad*203+cantidad*27.58)*0.8
    print(a)
  elif productos==[4,5]:
    b= (cantidad*348.00+cantidad*51.19)*0.75
    print(b)
  else:
    c= (cantidad*33.7+cantidad*203+cantidad*27.58+cantidad*348.00+cantidad*51.19)
    print(c)
  
  
  


