products = {
    1: {"name": "Juego Pokemon X para Nintendo 3DS", "price": 33.77},
    2: {"name": "Nintendo 3DS XL", "price": 203},
    3: {"name": "Juego Mario Kart 7 para Nintendo 3DS", "price": 27.58},
    4: {"name": "PlayStation 4", "price": 348.00},
    5: {"name": "FIFA 16, PlayStation 4", "price": 51.19}
}

cart = {}
discounted_total = 0

def add_to_cart(product_id, quantity):
    global discounted_total
    if product_id in cart:
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity
    
    if product_id in (1, 2, 3):
        discounted_total += products[product_id]["price"] * quantity * 0.8
    elif product_id in (4, 5):
        discounted_total += products[product_id]["price"] * quantity * 0.85

def view_cart():
    print("Productos en el carrito:")
    for product_id, quantity in cart.items():
        product = products[product_id]
        print(f"{quantity}x {product['name']}")
    print()

def checkout():
    global discounted_total
    print("Resumen de la compra:")
    view_cart()
    print(f"Total a pagar (con descuento): USD {round(discounted_total, 1)}")

while True:
    user_input = input("Ingrese el número de producto y la cantidad (ejemplo: 5,2), 'ver' para mostrar el carrito, o 'checkout' para finalizar la compra: ")

    if user_input == "checkout":
        checkout()
        break

    if user_input == "ver":
        view_cart()
        continue

    try:
        product_id, quantity = map(int, user_input.split(","))
        if product_id not in products:
            print("Producto no válido. Intente nuevamente.")
            continue
        if quantity <= 0:
            print("Cantidad no válida. Intente nuevamente.")
            continue
        add_to_cart(product_id, quantity)
        print("Producto agregado al carrito.")
    except ValueError:
        print("Entrada inválida. Intente nuevamente.")