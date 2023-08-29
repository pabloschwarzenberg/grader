# Precios de los productos
product_prices = {
    1: 33.77,
    2: 203.00,
    3: 27.58,
    4: 348.00,
    5: 51.19
}

# Carro de compras
shopping_cart = {}

# Descuentos
discounts = {
    '1,2,3': 0.20,
    '4,5': 0.15
}

# Función para agregar productos al carro
def add_to_cart(product_id, quantity):
    if product_id in shopping_cart:
        shopping_cart[product_id] += quantity
    else:
        shopping_cart[product_id] = quantity

# Función para calcular el total del carro con descuentos
def calculate_total():
    total = 0

    # Calcular el total sin descuentos
    for product_id, quantity in shopping_cart.items():
        price = product_prices[product_id]
        total += price * quantity

    # Aplicar descuentos
    for products, discount in discounts.items():
        product_ids = [int(p) for p in products.split(',')]
        if all(product_id in shopping_cart for product_id in product_ids):
            discount_amount = total * discount
            total -= discount_amount

    return round(total, 1)

# Obtener la entrada del usuario y procesar las órdenes
while True:
    order = input("Ingrese una orden (producto,cantidad / ver / checkout): ")

    if order == 'ver':
        # Mostrar los productos en el carro
        print("Productos en el carro:")
        for product_id, quantity in shopping_cart.items():
            print("Producto", product_id,":", quantity, "unidades")
    elif order == 'checkout':
        # Calcular el total y hacer el checkout
        total = calculate_total()
        print("Total a pagar: USD", total)
        break
    else:
        # Agregar productos al carro
        try:
            product_id, quantity = order.split(',')
            product_id = int(product_id)
            quantity = int(quantity)
            add_to_cart(product_id, quantity)
            print("Producto agregado al carro.")
        except ValueError:
            print("Orden inválida. Intente nuevamente.")