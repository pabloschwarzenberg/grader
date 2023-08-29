p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
# Definimos un diccionario con los productos y sus precios
productos = {
  "1": ("Juego Pokemon X para Nintendo 3DS", 33.77),
  "2": ("Nintendo 3DS XL", 203),
  "3": ("Juego Mario Kart 7 para Nintendo 3DS", 27.58),
  "4": ("PlayStation 4", 348),
  "5": ("FIFA 16, PlayStation 4", 51.19)
}

# Definimos una lista vacía para el carro de compras
carro = []

# Definimos una función que agrega un producto al carro
def agregar_producto(producto, cantidad):
  # Convertimos la cantidad a entero
  cantidad = int(cantidad)
  # Verificamos si el producto existe en el diccionario
  if producto in productos:
    # Obtenemos el nombre y el precio del producto
    nombre, precio = productos[producto]
    # Agregamos una tupla con el nombre, el precio y la cantidad al carro
    carro.append((nombre, precio, cantidad))
    # Imprimimos un mensaje de confirmación
    print("Se agregaron", cantidad," unidades de ", nombre,"al carro.")
  else:
    # Imprimimos un mensaje de error
    print("El producto no existe.")

# Definimos una función que muestra los productos del carro
def ver_productos():
  # Verificamos si el carro está vacío
  if not carro:
    # Imprimimos un mensaje de aviso
    print("El carro está vacío.")
  else:
    # Imprimimos un encabezado
    print("Productos en el carro:")
    # Recorremos los productos del carro
    for nombre, precio, cantidad in carro:
      # Imprimimos el nombre, el precio y la cantidad de cada producto
      print("- ", nombre,": $", precio," x ", cantidad)

# Definimos una función que calcula el valor total del carro con descuentos
def calcular_total():
  # Inicializamos variables para los subtotales y los descuentos
  subtotal_1 = 0 # Subtotal de los productos 1, 2 y 3
  subtotal_2 = 0 # Subtotal de los productos 4 y 5
  descuento_1 = 0 # Descuento de los productos 1, 2 y 3
  descuento_2 = 0 # Descuento de los productos 4 y 5
  total = 0 # Total del carro
  # Recorremos los productos del carro
  for nombre, precio, cantidad in carro:
    # Calculamos el valor de cada producto según su cantidad
    valor = precio * cantidad
    # Sumamos el valor al subtotal correspondiente según el nombre del producto
    if nombre in ["Juego Pokemon X para Nintendo 3DS", "Nintendo 3DS XL", "Juego Mario Kart 7 para Nintendo 3DS"]:
      subtotal_1 += valor
    elif nombre in ["PlayStation 4", "FIFA 16, PlayStation 4"]:
      subtotal_2 += valor
    else:
      # Si el producto no tiene descuento, lo sumamos directamente al total
      total += valor
  # Calculamos los descuentos según los subtotales
  if subtotal_1 > 0:
    descuento_1 = subtotal_1 * 0.2 # Descuento del 20%
    total += subtotal_1 - descuento_1 # Sumamos el subtotal menos el descuento al total
  if subtotal_2 > 0:
    descuento_2 = subtotal_2 * 0.15 # Descuento del 15%
    total += subtotal_2 - descuento_2 # Sumamos el subtotal menos el descuento al total
  # Retornamos el total redondeado a un decimal
  return round(total,1)

# Definimos una función que hace el checkout del carro
def hacer_checkout():
   # Verificamos si el carro está vacío 
   if not carro:
     # Imprimimos un mensaje de aviso 
     print("El carro está vacío.")
   else:
     # Calculamos el total del carro con descuentos 
     total = calcular_total()
     # Imprimimos el total 
     print("El valor total del carro es $", total)

# Definimos una función que procesa la entrada del usuario 
def procesar_entrada(entrada):
   # Dividimos la entrada por comas 
   partes = entrada.split(",")
   # Verificamos si la entrada es una orden válida 
   if entrada == "ver":
     # Llamamos a la función ver_productos() 
     ver_productos()
   elif entrada == "checkout":
     # Llamamos a la función hacer_checkout() 
     hacer_checkout()
   elif len(partes) == 2:
     # Llamamos a la función agregar_producto() con las partes de la entrada 
     agregar_producto(partes[0], partes[1])
   else:
     # Imprimimos un mensaje de error 
     print("Entrada inválida.")

# Definimos una variable para controlar el ciclo principal 
seguir = True

# Imprimimos un mensaje de bienvenida 
print("Bienvenido al prototipo de carro de compras de Amazon con Python.")

# Iniciamos el ciclo principal 
while seguir:
  # Solicitamos la entrada del usuario 
  entrada = input("Ingrese el producto y la cantidad que desea agregar al carro, o una orden (ver o checkout): ")
  # Procesamos la entrada del usuario 
  procesar_entrada(entrada)
  # Preguntamos al usuario si desea continuar 
  respuesta = input("¿Desea continuar? (s/n): ")
  # Verificamos la respuesta del usuario 
  if respuesta.lower() == "n":
    # Cambiamos el valor de la variable seguir para terminar el ciclo 
    seguir = False
    # Imprimimos un mensaje de despedida 
    print("Gracias por usar el prototipo de carro de compras de Amazon con Python.")