p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
carro=[[1,0,"Pokemon X",33.77],[2,0,"Nintendo XL",203],[3,0,"Mario Kart 7",27.58],[4,0,"PlayStation 4",348.00],[5,0,"FIFA 16",51.19]]
if __name__ == "__main__":
  pedido = input("Ingrese producto,cantidad")
  pedidoArray = pedido.split(",")
  producto = int(pedidoArray[0])
  cantidad = int(pedidoArray[1])
  pedido2 = input("Ingrese producto,cantidad")
  pedidoArray2 = pedido2.split(",")
  producto2 = int(pedidoArray2[0])
  cantidad2 = int(pedidoArray2[1])
  pedido3 = input("Ingrese producto,cantidad")
  pedidoArray3 = pedido3.split(",")
  producto3 = int(pedidoArray3[0])
  cantidad3 = int(pedidoArray3[1])
  carro[producto-1][1] = carro[producto-1][1]+cantidad
  carro[producto2-1][1] = carro[producto2-1][1]+cantidad2
  carro[producto3-1][1] = carro[producto3-1][1]+cantidad3
  opcion = input("ver o checkout")
  carrito1=carro[0][1]*carro[0][3]
  carrito2=carro[1][1]*carro[1][3]
  carrito3=carro[2][1]*carro[2][3]
  carrito4=carro[3][1]*carro[3][3]
  carrito5=carro[4][1]*carro[4][3]
  pond1= 0.8
  pond2= 0.85
  suma=round(carrito1+carrito2+carrito3+carrito4+carrito5,1)
  if carrito1 > 0 and carrito2 > 0 and carrito3 > 0:
   suma = (suma * 80)/100
  if carrito4 > 0 and carrito5 > 0:
   suma = (suma * 85)/100  
  if opcion == "ver":
   if not(carro[0][1] == 0):
    print(carro[0][2]," cantidad : ", carro[0][1], " subtotal : ", carro[0][1]*carro[0][3])
   if not(carro[1][1] == 0):
    print(carro[1][2]," cantidad : ", carro[1][1], " subtotal : ", carro[1][1]*carro[1][3])
   if not(carro[2][1] == 0):
    print(carro[2][2]," cantidad : ", carro[2][1], " subtotal : ", carro[2][1]*carro[2][3])
   if not(carro[3][1] == 0):
    print(carro[3][2]," cantidad : ", carro[3][1], " subtotal : ", carro[3][1]*carro[3][3])
   if not(carro[4][1] == 0): 
    print(carro[4][2]," cantidad : ", carro[4][1], " subtotal : ", carro[4][1]*carro[4][3])
  if opcion == "checkout":
   print("el valor esperado es ",suma)