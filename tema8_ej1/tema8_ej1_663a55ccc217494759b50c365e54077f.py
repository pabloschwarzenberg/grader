# Declaracion de funciones
def crear_cesta_compras(d):
    op="S"
    while (op=="S"):
        art = input("Ingresa un artículo: ")
        precio = float(input("Ingresa el precio de "+art+" : "))
        d[art] = precio
        op = input("¿Añadir otro artículo a la cesta S/N?: ")
        op = op.upper()

def mostrar_compra(d):
    total_compra = 0.0
    print("Lista de la compra:")
    for a in d:
        print(a,"\t",d[a])
        total_compra += d[a]
    print("Total:","\t",total_compra)

'''def mostrar_compra(d):
    total_compra = 0.0
    print("Lista de la compra:")
    for art,precio in d.items():
        print(art,"\t",precio)
        total_compra += precio
    print("Total:","\t",total_compra)'''

# Programa principal   
print("\nCesta de Compras")
op="S"
while (op=="S"):
    # Declaración del diccionario
    cesta = {}
    crear_cesta_compras(cesta)
    mostrar_compra(cesta)
    op=input("\nEjecutar otra vez? S/N: ")
    op = op.upper()
    