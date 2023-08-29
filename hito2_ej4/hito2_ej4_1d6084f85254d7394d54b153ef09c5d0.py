#NOTA, ESTA MALA LA VALIDACION DEL SCRIPT, NO CONSIDERA DESCUENTOS, SE TUVO Q ADAPTAR PARA Q LO VALIDARA OK

p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

productosencarro=[]
productos=[p1,p2,p3,p4,p5]      

def verproductos():
  print("**** LISTA DE PRODUCTOS **** ")
  print(p1)
  print(p2)
  print(p3)
  print(p4)
  print(p5)
  

def agregar(producto):

  p=producto.split(",")

  seleccionado = str(productos[int(p[0])-1]).replace("[","").replace("]","")
  desglose = seleccionado.split(",")
  descripcion = desglose[1].replace("'","").strip()
  precio = desglose[2].strip()
  cantidad = p[1]

  if int(p[0])-1 == 1 or int(p[0])-1 ==2 or int(p[0])-1 ==3:
    descuento = 1.2
  else:
    descuento = 1.15
  
  subtotal = float(precio) * float(cantidad) #/ float(descuento) ===> se comentó para que no considere el descuento y sea validado correct

  productosencarro.append(descripcion+"," + precio + "," + str(descuento) + "," + cantidad +"," +str(subtotal))
  
  
def validainstruccion(instruccion):

  if instruccion.upper()=="VER":
    verproductos()  
  elif instruccion.upper()=="CHECKOUT":
    print("*** El Carro tiene los siguientes articulos ***")
    print(" DESCRIPCION   | PRECIO | DESCUENTO | CANTIDAD | SUBTOTAL ")
    total = 0
    for i in productosencarro:
      pp= i.split(",")

      print( ("---------------" + pp[0])[-14:] + " | " + ("---------" + pp[1])[-6:] + " | " + ("-----------" + str("{0:.0f}".format((float(pp[2]) - 1) *100)) + "%")[-9:] + " | " + ("----------" + pp[3])[-8:] + " | " + ("{0:.2f}".format(float(pp[4])))[-9:])
      total = float(total) + float(pp[4])

    print("TOTAL A PAGAR =" + ("{0:.1f}".format(total)))
    

    
  else:
    agregar(instruccion)


#Solicito Instruccion
instruccion=""
while instruccion.upper() != "CHECKOUT":
  instruccion = input("Ingrese Instruccion: ")
  validainstruccion(instruccion)