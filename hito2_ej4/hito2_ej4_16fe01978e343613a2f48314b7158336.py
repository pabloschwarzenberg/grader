p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
carrito = []
# Funciones del carrito
def ver(carrito):
 lista = []
 for i in range(len(carrito)):
     lista.append(carrito[i])
     return lista
     
def descuentos(carrito):
     precio = 0
     for i in range(len(carrito)):
         precio = precio + carrito[i][2]
     if p1 in carrito and p2 in carrito and p3 in carrito:
        precio_final = 0.8 * precio
        return round(precio_final,1)
     if p4 in carrito and p5 in carrito:
        precio_final2 = precio * 0.85
        return round(precio_final2,1)
     else:
          return round(precio,1)
mirar = input("Desea ver el carrito:")
if mirar == "si":
        print(ver(carrito))
while True:
     producto = input("Ingrese el numero y la cantidad del producto que desea:")
     if producto[0]== "1" and producto[1]==","and len(producto)== 3:
         cantidad = int(producto[2])
         i = 0
         while i < cantidad:
               carrito.append(p1)
               i = i + 1
                 
     elif producto[0] == "2" and producto[1]=="," and len(producto)==3:
          cantidad2 = int(producto[2])
          j = 0
          while j < cantidad2:
                carrito.append(p2)
                j = j + 1
     elif producto[0] == "3" and len(producto)==3 and producto[1]==",":
          cantidad3 = int(producto[2])
          k = 0
          while k < cantidad3:
                carrito.append(p3)
                k = k + 1
     elif producto[0] == "4" and len(producto)==3 and producto[1]==",":
          cantidad4 = int(producto[2])
          l = 0
          while l < cantidad4:
                 carrito.append(p4)
                 l = l + 1
     elif producto[0] == "5" and len(producto)==3 and producto[1]==",":
         cantidad5 = int(producto[2])
         m = 0
         while m < cantidad5:
                 carrito.append(p5)
                 m = m + 1
     elif producto == "checkout":
         print(descuentos(carrito))
         break
     else:
        print("Producto inexistente")
        break
         
     

