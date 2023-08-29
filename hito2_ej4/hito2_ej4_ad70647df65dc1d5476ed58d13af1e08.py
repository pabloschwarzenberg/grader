# Definir los precios de los productos
PRODUCT_PRICES = {
    1: 33.77,
    2: 203.00,
    3: 27.58,
    4: 348.00,
    5: 51.19
}

# Definir los descuentos
DISCOUNTS = {
    "1,2,3": 0.2,
    "4,5": 0.15
}

# Inicializar el carro de compras
shopping_cart = {}

def add_product(product, quantity):
    product = int(product)
    if product in PRODUCT_PRICES:
        if product in shopping_cart:
            shopping_cart[product] += int(quantity)
        else:
            shopping_cart[product] = int(quantity)
        print("Producto agregado al carro.")
    else:
        print("El producto no existe.")

def show_cart():
    if shopping_cart:
        print("Productos en el carro:")
        for product, quantity in shopping_cart.items():
            print(f"Producto {product}: {quantity} unidades")
    else:
        print("El carro de compras está vacío.")

def checkout():
    total_price = 0

    for product, quantity in shopping_cart.items():
        if product in PRODUCT_PRICES:
            price = PRODUCT_PRICES[product]
            total_price += price * quantity

    discount_key = ",".join(str(product) for product in shopping_cart.keys())
    if discount_key in DISCOUNTS:
        discount = DISCOUNTS[discount_key]
        total_price -= total_price * discount

    print("Carro de compras:")
    show_cart()
    print("Total a pagar: $", round(total_price, 1))

# Ciclo principal del programa
while True:
    order = input("Ingrese una orden (producto,cantidad / ver / checkout): ")

    if order == "ver":
        show_cart()
    elif order == "checkout":
        checkout()
        break
    else:
        try:
            product, quantity = order.split(",")
            add_product(product, quantity)
        except ValueError:
            print("Orden inválida.")

