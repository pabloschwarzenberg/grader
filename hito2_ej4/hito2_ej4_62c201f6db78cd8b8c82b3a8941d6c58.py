class ShoppingCart:
    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity):
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

    def calculate_total(self):
        total = 0.0
        discount = 0.0

        if '1' in self.products and '2' in self.products and '3' in self.products:
            discount = 0.2
        elif '4' in self.products and '5' in self.products:
            discount = 0.15

        for product, quantity in self.products.items():
            total += self.get_product_price(product) * quantity

        total -= total * discount
        return round(total, 1)

    def get_product_price(self, product):
        prices = {
            '1': 33.77,
            '2': 203,
            '3': 27.58,
            '4': 348.00,
            '5': 51.19
        }

        return prices[product]

    def print_cart(self):
        for product, quantity in self.products.items():
            print(f'Producto {product}: {quantity} unidades')

# Función principal del programa
def run_program():
    shopping_cart = ShoppingCart()

    while True:
        user_input = input('Ingrese una orden (producto,cantidad / ver / checkout): ')

        if user_input == 'ver':
            shopping_cart.print_cart()
        elif user_input == 'checkout':
            total = shopping_cart.calculate_total()
            print(f'El total a pagar es: USD {total}')
            break
        else:
            try:
                product, quantity = user_input.split(',')
                shopping_cart.add_product(product, int(quantity))
            except ValueError:
                print('Entrada inválida. Intente nuevamente.')

# Ejecutar el programa
run_program()
