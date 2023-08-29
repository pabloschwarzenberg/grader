def menu():
    print()
    print("Algo que te puede gustar")
    print()
    print("1: Pokemon X/ Nintendo 3DS/ USD 33.77")
    print("2: Nintendo 3DS XL/ USD 203")
    print("3: Mario Kart 7/ Nintendo 3DS/ USD 27.58")
    print("4: PlayStation 4/ USD 348.00")
    print("5: FIFA 16/ PlayStation 4/ USD 51.19")
    print()
""" 
def desc(carrito,total_pago):
    for i in range(len(carrito)):
            if carrito[i][0]== 1 and 2 and 3: 
                descuento= total_pago* 0.2
                total_pago=total_pago-descuento
                #print(round(total_pago, 1))
                
            elif carrito[i][0]==4 and 5:
                descuento=total_pago*0.15
                total_pago=total_pago-descuento
                #print(round(total_pago, 1))
            
    return total_pago
         """

def imprimir_productos(carrito):
    print(carrito)

def check():
    print("Productos........." + str(carrito))
    print("Total pago........." + str(round(total_pago, 1)))
    

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
menu()

carrito=[]
ver_carrito="no"
checkout="no"
total_pago=0
total_pago1=0

while ver_carrito != "ver":
    compra=int(input("Indique que desea llevar= " ))
    cantidad=int(input("Indique cuantas unidades= "))
    carrito.append([compra,cantidad])  
        
    if compra==1:
        total_pago= total_pago + 33.77*cantidad
    elif compra==2:
        total_pago= total_pago + 203*cantidad
    elif compra==3:
        total_pago= total_pago + 27.58*cantidad
    elif compra==4:
        total_pago= total_pago + 348.00*cantidad
    elif compra==5:
        total_pago= total_pago + 51.19*cantidad
    
    ver_carrito=input("¿Desea visualizar el carrito?(ver/no): ")
        #print(total_pago)
        #print(carrito)
    
    if len(carrito)!=1:
        for i in range(len(carrito)):
            if carrito[i][0]== 1 and 2 and 3: 
                descuento= total_pago* 0.20
                total_pago=total_pago-descuento
                #print(round(total_pago, 1))
                
            elif carrito[i][0]==4 and 5:
                descuento=total_pago*0.15
                total_pago=total_pago-descuento
                #print(round(total_pago, 1))
    
    if ver_carrito=="ver":
        imprimir_productos(carrito)

checkout=input("¿Desea realizar el checkout?(si/no): ")

if checkout=="si":
    check()
#




      