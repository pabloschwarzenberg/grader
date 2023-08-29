p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

precios={1: p1[2],2: p2[2],3: p3[2],4: p4[2],5: p5[2]}

carro={}

def Agregar(p, c):
	
	if p in carro:
		
		carro[p]+=c
		
	else:
		
		carro[p]=c

def Vercarro():
	
	if not carro:
		
		print('El carro esta vacio.')
		
	else:
		
		for p, c in carro.items():
			
			n=""
			
			if p==1:
				
				n=p1[1]
				
			elif p==2:
				
				n=p2[1]
				
			elif p==3:
				
				n=p3[1]
				
			elif p==4:
				
				n=p4[1]
				
			elif p==5:
				
				n=p5[1]

			print('producto: '+str(n)+' - cantidad: '+str(c))

def Checkout():
	
	T=0

	if len(carro)>=3 and all(p in carro for p in [1, 2, 3]):

		subT=sum(precios[p] * carro[p] for p in carro)
		des=subT*0.2
		T=subT-des
		
	elif len(carro)>=2 and all(p in carro for p in [4, 5]):

		subT=sum(precios[p] * carro[p] for p in carro)
		des=subT * 0.15
		T=subT-des
		
	else:

		T=sum(precios[p] * carro[p] for p in carro)

	return round(T, 1)
	
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print('')

while (1):
	
	op=input('Ingrese una seleccion (producto, cantidad / ver / checkout): ')

	if op=='ver':
		
		Vercarro()
		
	elif op=='checkout':
		
		T=Checkout()
		print('El total a pagar es: '+str(T))
		break
		
	else:
		
		s=op.split(",")
		
		if len(s)==2:
			
			p=int(s[0])
			c=int(s[1])
			Agregar(p, c)