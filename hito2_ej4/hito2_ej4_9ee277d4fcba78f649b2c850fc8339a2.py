# Definir los productos y sus precios
products = {
    1: {"name": "Juego Pokemon X para Nintendo 3DS", "price": 33.77},
    2: {"name": "Nintendo 3DS XL", "price": 203},
    3: {"name": "Juego Mario Kart 7 para Nintendo 3DS", "price": 27.58},
    4: {"name": "PlayStation 4", "price": 348.00},
    5: {"name": "FIFA 16, PlayStation 4", "price": 51.19}
}

# Inicializar el carro de compras
shopping_cart = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0
}

# Función para agregar productos al carro
def add_to_cart(product, quantity):
    if product in shopping_cart:
        shopping_cart[product] += quantity
    else:
        print("Producto no válido.")

# Función para mostrar los productos en el carro
def show_cart():
    print("Productos en el carro:")
    total_price = 0
    for product, quantity in shopping_cart.items():
        if quantity > 0:
            product_name = products[int(product)]["name"]
            product_price = products[int(product)]["price"]
            total_price += product_price * quantity
            print(f"Producto: {product_name}, Cantidad: {quantity}")

    print(f"Precio total: ${round(total_price, 1)}")

# Función para hacer el checkout
def checkout():
    total_price = 0
    for product, quantity in shopping_cart.items():
        if quantity > 0:
            product_price = products[int(product)]["price"]
            if product in ["1", "2", "3"]:
                product_price *= 0.8  # Aplicar descuento del 20%
            elif product in ["4", "5"]:
                product_price *= 0.85  # Aplicar descuento del 15%
            total_price += product_price * quantity

    print(f"Total a pagar: ${round(total_price, 1)}")

# Programa principal
if __name__ == "__main__":
    while True:
        action = input("Ingrese una acción (producto,cantidad / ver / checkout): ")

        if action == "ver":
            show_cart()
        elif action == "checkout":
            checkout()
            break
        else:
            try:
                product, quantity = action.split(",")
                add_to_cart(product, int(quantity))
            except ValueError:
                print("Entrada no válida.")
