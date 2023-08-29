
p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
carro=[[1,0,"Pokemon X",33.77],[2,0,"Nintendo XL",203],[3,0,"Mario Kart 7",27.58],[4,0,"PlayStation 4",348.00],[5,0,"FIFA 16",51.19]]
while True:
  pedido = input("Ingrese producto,cantidad")
  pedidoArray = pedido.split(",")
  producto = int(pedidoArray[0])
  cantidad = int(pedidoArray[1])
  carro[producto-1][1] = carro[producto-1][1]+cantidad
  opcion = input("ver o checkout")
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
    descuento = 0
    if not(carro[0][1] == 0) and not(carro[1][1] == 0) and not(carro[2][1] == 0):
      descuento += 0.2
    if not(carro[3][1] == 0) and not(carro[4][1] == 0):
      descuento += 0.15
    print(round((carro[0][3] * (1-descuento))*carro[0][1],1))
    print(round((carro[1][3] * (1-descuento))*carro[1][1],1))
    print(round((carro[2][3] * (1-descuento))*carro[2][1],1))
    print(round((carro[3][3] * (1-descuento))*carro[3][1],1))
    print(round((carro[4][3] * (1-descuento))*carro[4][1],1))