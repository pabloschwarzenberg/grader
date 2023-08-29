Aquí tienes un programa en Python que permite agregar productos al carro, mostrarlos y realizar el checkout con los descuentos correspondientes:

```python
# Diccionario de productos con sus precios
products = {
    '1': {'name': 'Juego Pokemon X para Nintendo 3DS', 'price': 33.77},
    '2': {'name': 'Nintendo 3DS XL', 'price': 203},
    '3': {'name': 'Juego Mario Kart 7 para Nintendo 3DS', 'price': 27.58},
    '4': {'name': 'PlayStation 4', 'price': 348.00},
    '5': {'name': 'FIFA 16, PlayStation 4', 'price': 51.19}
}

# Carro de compras
cart = {}

def add_to_cart(product_id, quantity):
    if product_id in products:
        if product_id in cart:
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity
        print(f"Se agregaron {quantity} unidades del producto {product_id} al carro.")
    else:
        print("Producto inválido.")

def view_cart():
    if len(cart) > 0:
        print("Productos en el carro:")
        for product_id, quantity in cart.items():
            product = products[product_id]
            name = product['name']
            price = product['price']
            total_price = price * quantity
            print(f"{name} (x{quantity}): USD {total_price:.2f}")
    else:
        print("El carro está vacío.")

def checkout():
    total_price = 0.0

    # Calcular precio total
    for product_id, quantity in cart.items():
        product = products[product_id]
        price = product['price']
        total_price += price * quantity

    # Aplicar descuento
    if '1' in cart and '2' in cart and '3' in cart:
        total_price *= 0.8
    elif '4' in cart and '5' in cart:
        total_price *= 0.85

    # Imprimir el valor total del carro
    print(f"Total a pagar: USD {round(total_price, 1)}")

# Programa principal
while True:
    action = input("Ingrese una acción (agregar, ver, checkout): ")

    if action == 'agregar':
        product_info = input("Ingrese el ID del producto y la cantidad separados por coma: ")
        product_id, quantity = product_info.split(',')
        add_to_cart(product_id, int(quantity))
    elif action == 'ver':
        view_cart()
    elif action == 'checkout':
        checkout()
        break
    else:
        print("Acción inválida.")
```

Este programa utiliza un diccionario `products` para almacenar los productos con sus respectivos precios. El carro de compras se representa mediante otro diccionario `cart`, donde las claves son los IDs de los productos y los valores son las cantidades.

El programa define tres funciones:
- `add_to_cart`: Agrega productos al carro. Verifica si el producto es válido y actualiza la cantidad en el carro.
- `view_cart`: Muestra los productos y cantidades en el carro, junto con el precio total de cada producto.
- `checkout`: Calcula el precio total del carro teniendo en cuenta los descuentos y lo muestra redondeado a un decimal.

En el programa principal, se utiliza un bucle infinito para recibir las acciones del usuario. Dependiendo de la acción ingresada, se llama a la función
      