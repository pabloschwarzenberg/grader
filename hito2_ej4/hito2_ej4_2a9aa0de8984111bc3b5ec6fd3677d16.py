p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

precios={
	1: p1[2],
	2: p2[2],
	3: p3[2],
	4: p4[2],
	5: p5[2]
}

carro={}

def Agregar(producto, cantidad):
	
	if producto in carro:
		
		carro[producto]+=cantidad
		
	else:
		
		carro[producto]=cantidad

def VerCarro():
	
	if not carro:
		
		print('El carro esta vacio.')
		
	else:
		
		for producto, cantidad in carro.items():
			
			nombre=""
			
			if producto==1:
				
				nombre=p1[1]
				
			elif producto==2:
				
				nombre=p2[1]
				
			elif producto==3:
				
				nombre=p3[1]
				
			elif producto==4:
				
				nombre=p4[1]
				
			elif producto==5:
				
				nombre=p5[1]

			print('Producto: '+str(nombre)+' - Cantidad: '+str(cantidad))

def Checkout():
	
	total=0

	if len(carro)>=3 and all(producto in carro for producto in [1, 2, 3]):

		subtotal=sum(precios[producto] * carro[producto] for producto in carro)
		descuento=subtotal*0.2
		total=subtotal-descuento
		
	elif len(carro)>=2 and all(producto in carro for producto in [4, 5]):

		subtotal=sum(precios[producto] * carro[producto] for producto in carro)
		descuento=subtotal * 0.15
		total=subtotal-descuento
		
	else:

		total=sum(precios[producto] * carro[producto] for producto in carro)

	return round(total, 1)
	
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print('')

while True:
	
	orden=input('Ingrese una orden (producto,cantidad / ver / checkout): ')

	if orden=='ver':
		
		VerCarro()
		
	elif orden=='checkout':
		
		total=Checkout()
		print('El total a pagar es: '+str(total))
		break
		
	else:
		
		ordensep=orden.split(",")
		
		if len(ordensep)==2:
			
			producto=int(ordensep[0])
			cantidad=int(ordensep[1])
			Agregar(producto, cantidad)
      