p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16", 51.19]

cart = {}

def add_product_to_cart(product, quantity):
    if product in cart:
        cart[product] += quantity
    else:
        cart[product] = quantity

def calculate_total_price():
    total_price = 0

    for product, quantity in cart.items():
        if product == 1 or product == 2 or product == 3:
            total_price += p1[2] * quantity
        elif product == 4 or product == 5:
            total_price += p4[2] * quantity

    if 1 in cart and 2 in cart and 3 in cart:
        total_price *= 0.8  # 20% discount
    elif 4 in cart and 5 in cart:
        total_price *= 0.85  # 15% discount

    return round(total_price, 1)

while True:
    user_input = input("Ingrese un comando ('producto,cantidad', 'ver', 'checkout'): ")
    command = user_input.split(',')

    if command[0] == 'ver':
        print("Carro de compras:")
        for product, quantity in cart.items():
            if product == 1:
                print(f"{p1[1]} x {quantity}")
            elif product == 2:
                print(f"{p2[1]} x {quantity}")
            elif product == 3:
                print(f"{p3[1]} x {quantity}")
            elif product == 4:
                print(f"{p4[1]} x {quantity}")
            elif product == 5:
                print(f"{p5[1]} x {quantity}")
        print()

    elif command[0] == 'checkout':
        total_price = calculate_total_price()
        print(f"Total a pagar: ${total_price}")
        break

    else:
        try:
            product = int(command[0])
            quantity = int(command[1])
            add_product_to_cart(product, quantity)
            print("Producto agregado al carro.")
        except:
            print("Comando inválido. Por favor, intente de nuevo.")
