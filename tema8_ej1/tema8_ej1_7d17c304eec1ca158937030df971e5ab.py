class Producto:
	
	def __init__(self, codigo, nombre, stock, precio):
		
		self.codigo=codigo
		self.stock=stock
		self.precio=precio
		self.nombre=nombre

	def __eq__(self, other):
		
		if self.codigo==other.codigo:
			
			return True
			
		else:
			
			return False


class Item:
	
	def __init__(self, cantidad, producto):
		
		self.cantidad=cantidad
		self.producto=producto


class Carro:
	
	def __init__(self):
		
		self.lista_de_productos=[]
		self.descuento=0
		self.total=0
		self.ruta=''

	def agregar_item(self, cantidad, producto):
		
		for item in self.lista_de_productos:
			
			if item.producto==producto:
				
				if cantidad==0:
					
					self.lista_de_productos.remove(item)
					
				else:
					
					item.cantidad=cantidad
					
				return
				
		item=Item(cantidad, producto)
		self.lista_de_productos.append(item)

	def checkout(self, despacho, ruta):
		
		subtotal=sum(item.producto.precio * item.cantidad for item in self.lista_de_productos)
		descuento=0
		
		if len(self.lista_de_productos)>=3 and all(item.producto.codigo in [1, 2, 3] for item in self.lista_de_productos):
			
			descuento=subtotal * 0.2
			
		elif len(self.lista_de_productos)>=2 and all(item.producto.codigo in [4, 5] for item in self.lista_de_productos):
			
			descuento=subtotal * 0.15

		delivery=0
		
		if despacho==0: 
			
			delivery=(subtotal-descuento)*0.2
			
		elif despacho==1: 
			
			delivery=(subtotal - descuento)*0.3

		total=subtotal-descuento+delivery

		if "chile" in ruta.lower():
			
			total*=1.2

		return round(total, 0)

	def __repr__(self):
		
		car='Carro de Compras:\n'
		
		for item in self.lista_de_productos:
			
			car=car+'{0}: {1}\n'.format(item.cantidad, item.producto.nombre)
			
		return car


class Tienda:
	
	def __init__(self):
		
		self.catalogo=[]
		producto=Producto(1, 'Juego Pokemon Y:', 10, 31.51)
		self.catalogo.append(producto)
		producto=Producto(2, 'Nintendo 3DS:', 5, 190.95)
		self.catalogo.append(producto)
		producto=Producto(3, 'Juego Mario Kart:', 10, 29.96)
		self.catalogo.append(producto)
		producto=Producto(4, 'Playstation 4:', 10, 399)
		self.catalogo.append(producto)
		producto=Producto(5, 'Fifa 14:', 10, 41.95)
		self.catalogo.append(producto)

	def menu(self):
		
		for producto in self.catalogo:
			
			print('{0}: {1} ${2}'.format(producto.codigo, producto.nombre, producto.precio))

	def buscarProducto(self, numero):
		
		for producto in self.catalogo:
			
			if producto.codigo==numero:
				
				return producto


if __name__=='__main__':
	
	tienda=Tienda()
	carro=Carro()
	
	while (1):
		
		tienda.menu()
		item_ingresado=input('Ingrese un numero: ')
		
		if item_ingresado=='':
			
			break
			
		else:
			
			item_ingresado=item_ingresado.split(",")
			numero=int(item_ingresado[0])
			producto=tienda.buscarProducto(numero)
			cantidad=int(item_ingresado[1])
			carro.agregar_item(cantidad, producto)
			
		print(carro)

	print(carro.checkout(0, "usa"))
	print(carro.checkout(1, "usa"))
	print(carro.checkout(0, "Alameda 340 Santiago Chile"))
	print(carro.checkout(1, "Alameda 340 Santiago Chile"))