p1 = [1, "Pokemon  X", 33.77]
p2 = [2, "Nintendo XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "Playstation 4", 348.00]
p5 = [5, "FIFA 16", 51.19]
# Todos los productos de la tienda
productos = []
productos.append(p1)
productos.append(p2)
productos.append(p3)
productos.append(p4)
productos.append(p5)
# Carro de compras del usuario
carro = []
# Funcion para agregar productos al carro
def agregar_producto(producto_id, cantidad, carro, productos):
	# Agregar al carro el producto
	for a in range(0, int(cantidad)):
		carro.append(productos[int(producto_id) -1])

def hacer_checkout(carro):
	precio_final = 0
	# Recorrer carro
	for a in carro:
		precio_final += a[2]
	return precio_final
# Menu
while True:
	# Imprimir funciones que puede hacer el usuario
	print("1. Agregar producto al carro")
	print("2. Ver productos del carro")
	print("3. Hacer checkout")
	eleccion_usuario = input("Que quieres hacer: ")
	if eleccion_usuario == "1" or eleccion_usuario == 1:
		print("\n")
		for p in productos:
			print("Id producto: " + str(p[0]))
			print("Nombre del producto: " + p[1])
			print("Precio del producto: $" + str(p[2]))
			print("-------------------------------------------")
		producto_usuario = input("Ingresa el producto y la cantidad en el formato correcto (producto, cantidad): ")
		# Se asume que el usuario ingresará un producto válido en el formato entregado
		producto = producto_usuario.split(",")[0]
		cantidad = producto_usuario.split(",")[1]
		agregar_producto(producto, cantidad, carro, productos)
		print("\n")

	if eleccion_usuario == "2" or eleccion_usuario == 2 or eleccion_usuario == "ver":
		print("\n")
		print("---------------------------")
		print("Carro de compras")
		print("---------------------------")
		for p in carro:
			print("Id producto: " + str(p[0]))
			print("Nombre del producto: " + p[1])
			print("Precio del producto: $" + str(p[2]))
			print("-------------------------------------------")
		print("\n")

	if eleccion_usuario == "3" or eleccion_usuario == 3 or eleccion_usuario == "checkout":
		print("\n")
		print("----------------------------------------")
		print("Checkout")
		print("----------------------------------------")
		print("Precio final: " + str(hacer_checkout(carro)))
		print("\n")
		# Se asume que al hacer checkout se termina el programa
		break      