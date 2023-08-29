p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

lista=[]
def carro(producto,cantidad):
    for i in range(cantidad):
        lista.append(producto)

def checkout(lista):
    suma_total=0
    for i in lista:
        suma_total=suma_total+i[2]
    if p1 in lista and p2 in lista and p3 in lista:
        suma_total=suma_total*0.8
    elif p4 in lista and p5 in lista:
        suma_total=suma_total*0.85
    return round(suma_total,1)
while True:
    producto=input('''Que producto desea agregar y cuanta cantidad
1. Pokemon X
2. Nintendo XL
3. Mario Kart
4. PlayStatyon 4
5. FIFA 16
''')
   
    if producto[0]=='1':
        carro(p1,int(producto[-1]))
    elif producto[0]=='2':
        carro(p2,int(producto[-1]))
    elif producto[0]=='3':
        carro(p3,int(producto[-1]))
    elif producto[0]=='4':
        carro(p4,int(producto[-1]))
    elif producto[0]=='5':
        carro(p5,int(producto[-1]))
    
    if producto=='ver':
        print(lista)

    elif producto=='checkout':
        print(checkout(lista))
        break
        
