#Funciones de Diseño
def MuestraCarro():
    global carro
    
    for i in range(len(carro)):
        print(carro[i])

def CheckOut():
    global productos , cantidad
    preciofinal = 0
    descDS = [False,False,False]
    descPS = [False,False]
    for i in range(len(productos)):
        if (productos[i] == 1):
            preciofinal += 33.77 * cantidad[i]
             
        if (productos[i] == 2):
            preciofinal += 203 * cantidad[i]
            
        if (productos[i] == 3):
             preciofinal += 27.58 * cantidad[i]
             
        if (productos[i] == 4):
            preciofinal += 348 * cantidad[i]
            
        if (productos[i] == 5):
             preciofinal += 51.19 * cantidad[i]
  
    for i in range (len(productos)):
       if (productos[i] == 1):
           descDS[0] = True
           
       if (productos[i] == 2):
           descDS[1] = True
           
       if (productos[i] == 3):
           descDS[2] = True
           
       if (productos[i] == 4):
           descPS[0] = True
           
       if (productos[i] == 5):
           descPS[1] = True
           
       if (descDS[0] and descDS[1] and descDS[2]):
           preciofinal = preciofinal - preciofinal * 0.2
            
       if (descPS[0] and descPS[1]):
           preciofinal = preciofinal - preciofinal * 0.15
           
    print(preciofinal)
def AnadirProductos():
   global productos , cantidad    
   MostrarProductos()
   n = int(input("Ingrese la opcion del 1 al 5: "))
   cantidadproducto = int(input("Ingrese la cantidad de este producto que desea: "))

   productos.append(n)
   cantidad.append(cantidadproducto)

def MostrarProductos():
    print("1- Pokemon X , Precio: 33.77USD\n2- Nintendo XL , Precio: 203USD")
    print("3-Mario Kart 7 , Precio: 27.58\n4- PlayStation 4 , Precio: 348USD\n5- FIFA 16 , Precio: 51.19USD")  

    
#Juegos y precio correspondiente
p1=[1,"Pokemon X",33.77] #Nº de orden , objeto , precio
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348]
p5=[5,"FIFA 16",51.19]
productos = []
cantidad = [] #Producto , Cantidad 
#Finalizacion de variables
while True:
    opcion = 0
    print("1- Añadir Producto\n2-Mostrar Carro\n3-Checkout\n4-Salir")
    opcion = int(input("Ingrese la opcion que desea: "))
    
    if opcion == 1:
        AnadirProductos()
        
    if opcion == 2:
        MuestraCarro()
        
    if opcion == 3:
        CheckOut()
            
    if opcion == 4:
        break
 