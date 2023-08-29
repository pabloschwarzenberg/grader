precio = productos[producto]["precio"]
subtotal = cantidad * precio
print({nombre} (Cantidad,{cantidad}) - Subtotal, ${subtotal}"))
# Función para hacer el checkout y calcular el valor total con descuento
def checkout():
    total = 0
    for producto, cantidad in carro.items():
        precio = productos[producto]["precio"]
        subtotal = cantidad * precio
        total += subtotal
    if "1" in carro and "2" in carro and "3" in carro:
        total *= 0.8  # Aplicar descuento del 20%
    elif "4" in carro and "5" in carro:
        total *= 0.85  # Aplicar descuento del 15%
    total = round(total, 1)
    print(f"Total a pagar: ${total}")
# Programa principal
while True:
    orden = input("Ingrese la orden (agregar, ver, checkout): ")
    if orden == "agregar":
        datos = input("Ingrese el producto y la cantidad (producto,cantidad): ")
        producto, cantidad = datos.split(",")
        agregar_producto(producto, int(cantidad))
    elif orden == "ver":
        mostrar_carro()
    elif orden == "checkout":
        checkout()
        break
    else:
        print("Orden inválida. Intente nuevamente.")
