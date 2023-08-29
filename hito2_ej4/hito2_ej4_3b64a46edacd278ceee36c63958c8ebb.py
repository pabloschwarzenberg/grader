p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19] 

productos = [p1,p2,p3,p4,p5]
compras = []
total = 0
def ImprimirProductos(lista):
	for i in lista:
		print(i[0],i[1],i[2])

while(True):
	producto = input("Ingrese producto y cantidad (p,c): ").lower()
	if ("," in list(producto)):
		productoActual = producto.split(",")
		productoActual.insert(0,int(productoActual[0])-1)
		productoActual.pop(1)
		for i in productos:
			if(int(productoActual[0])+1 in i):
				if (not(productos[int(productoActual[0])] in compras)):
					compras.append(productos[int(productoActual[0])])
				total += productos[int(productoActual[0])][2]*int(productoActual[1])
	elif(producto == "ver"):
		ImprimirProductos(productos)
	elif(producto == "checkout"):
#		if (p1 in compras and p2 in compras and p3 in compras and p4 in compras and p5 in compras):
#			total = total - total*0.35
#		elif (p1 in compras and p2 in compras and p3 in compras):
#			total = total - total*0.2
#		elif(p3 in compras and p4 in compras):
#			total = total - total*0.15
		print(round(total,1))
		break
		
	else:
		print("Producto no valido")
		Producto = input("Ingrese producto y cantidad (p,c): ").lower()