# Diccionario que almacena los productos y sus precios
productos = {
  "1": ("Juego Pokemon X para Nintendo 3DS", 33.77),
  "2": ("Nintendo 3DS XL", 203),
  "3": ("Juego Mario Kart 7 para Nintendo 3DS", 27.58),
  "4": ("PlayStation 4", 348),
  "5": ("FIFA 16, PlayStation 4", 51.19)
}

# Lista que almacena los productos en el carro
carro = []

# Función que agrega un producto al carro
def agregar(producto, cantidad):
  # Verificar que el producto sea válido
  if producto in productos:
    # Agregar el producto y la cantidad al carro
    carro.append((producto, cantidad))
    # Imprimir un mensaje de confirmación
    print(f"Se agregó {cantidad} unidad(es) del producto {producto}: {productos[producto][0]}")
  else:
    # Imprimir un mensaje de error
    print(f"El producto {producto} no existe")

# Función que muestra los productos en el carro
def ver():
  # Verificar que el carro no esté vacío
  if carro:
    # Imprimir los productos y sus cantidades
    print("Los productos en el carro son:")
    for producto, cantidad in carro:
      print(f"{cantidad} unidad(es) del producto {producto}: {productos[producto][0]}")
  else:
    # Imprimir un mensaje de aviso
    print("El carro está vacío")

# Función que calcula el valor de los productos en el carro considerando los descuentos
def checkout():
  # Verificar que el carro no esté vacío
  if carro:
    # Inicializar el valor total y los subtotales de cada oferta
    total = 0
    subtotal1 = 0 # Oferta de los productos 1, 2 y 3
    subtotal2 = 0 # Oferta de los productos 4 y 5
    
    # Recorrer los productos en el carro y sumar sus precios a los subtotales correspondientes
    for producto, cantidad in carro:
      precio = productos[producto][1]
      if producto in ["1", "2", "3"]:
        subtotal1 += precio * cantidad
      elif producto in ["4", "5"]:
        subtotal2 += precio * cantidad
    
    # Aplicar los descuentos a los subtotales si se cumplen las condiciones
    if subtotal1 > 0:
      subtotal1 *= 0.8 # Descuento del 20%
    if subtotal2 > 0:
      subtotal2 *= 0.85 # Descuento del 15%
    
    # Sumar los subtotales al valor total y redondearlo a un decimal
    total = round(subtotal1 + subtotal2, 1)
    
    # Imprimir el valor total
    print(f"El valor de los productos en el carro es: USD {total}")
    
  else:
    # Imprimir un mensaje de aviso
    print("El carro está vacío")

# Programa principal que recibe las entradas y llama a las funciones correspondientes
while True:
  # Recibir la entrada del usuario
  entrada = input("Ingrese lo que quiere hacer: ")
  
  # Verificar si la entrada es válida
  if entrada == "ver":
    # Llamar a la función ver
    ver()
  
  elif entrada == "checkout":
    # Llamar a la función checkout y terminar el programa
    checkout()
    break
  
  elif "," in entrada:
    # Separar la entrada por la coma y obtener el producto y la cantidad
    producto, cantidad = entrada.split(",")
    
    # Verificar si la cantidad es un número entero positivo
    try:
      cantidad = int(cantidad)
      if cantidad > 0:
        # Llamar a la función agregar con el producto y la cantidad
        agregar(producto, cantidad)
      else:
        # Imprimir un mensaje de error
        print("La cantidad debe ser un número entero positivo")
    
    except ValueError:
      # Imprimir un mensaje de error
      print("La cantidad debe ser un número entero positivo")
  
  else:
    # Imprimir un mensaje de error
    print("La entrada no es válida")

      