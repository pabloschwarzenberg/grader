def add_to_cart(cart, product, quantity):
    if product in cart:
        cart[product] += quantity
    else:
        cart[product] = quantity

def calculate_discounted_price(cart):
    total_price = 0
    discount = 0

    if '1' in cart and '2' in cart and '3' in cart:
        discount = 0.2
    elif '4' in cart and '5' in cart:
        discount = 0.15

    for product, quantity in cart.items():
        if product == '1':
            total_price += 33.77 * quantity
        elif product == '2':
            total_price += 203 * quantity
        elif product == '3':
            total_price += 27.58 * quantity
        elif product == '4':
            total_price += 348 * quantity
        elif product == '5':
            total_price += 51.19 * quantity

    discounted_price = total_price - (total_price * discount)
    return round(discounted_price, 1)

def print_cart(cart):
    print("Carro de compras:")
    for product, quantity in cart.items():
        print("Producto", product, "- Cantidad:", quantity)

# Crear el carro de compras
cart = {}

while True:
    action = input("Ingresa una orden (producto,cantidad / ver / checkout): ")

    if action == "ver":
        print_cart(cart)
    elif action == "checkout":
        total_price = calculate_discounted_price(cart)
        print("Total a pagar:", total_price)
        break
    else:
        try:
            product, quantity = action.split(",")
            add_to_cart(cart, product, int(quantity))
        except:
            print("Orden inválida. Por favor, ingresa en el formato correcto (producto,cantidad).")
