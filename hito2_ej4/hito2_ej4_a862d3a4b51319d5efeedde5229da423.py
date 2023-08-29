
p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16", 51.19]

products = {1: p1, 2: p2, 3: p3, 4: p4, 5: p5}
cart = {}

while True:
    command = input("Enter a command (product,quantity / ver / checkout): ")

    if command == "ver":
        print("Cart contents:")
        for product, quantity in cart.items():
            product_info = products.get(product)
            if product_info:
                product_name = product_info[1]
                product_price = product_info[2]
                print("Product {}: {} - Quantity {} - Price: ${}".format(product, product_name, quantity, product_price))

    elif command == "checkout":
        total_price = 0
        discount = 0

        if {1, 2, 3}.issubset(cart.keys()):
            discount = 0.2
        elif {4, 5}.issubset(cart.keys()):
            discount = 0.15

        for product, quantity in cart.items():
            product_info = products.get(product)
            if product_info:
                product_price = product_info[2]
                total_price += quantity * product_price

        total_price -= total_price * discount
        total_price = round(total_price, 1)
        print("Total price: ${}".format(total_price))
        break

    else:
        try:
            product, quantity = map(int, command.split(","))
            if 1 <= product <= 5 and quantity >= 1:
                if product in cart:
                    cart[product] += quantity
                else:
                    cart[product] = quantity
            else:
                print("Invalid product or quantity.")
        except:
            print("Invalid command.")