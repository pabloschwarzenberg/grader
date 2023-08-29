# Importación de módulos
import os
import time

# Declaración de funciones
def crea_arch_ventas(av):
    try: 
        f = open(av,"r")
    except FileNotFoundError:
        f = open(av,"w")
        f.close()
    else:
        f.close()

def procesar_venta(ap,av):
    f = open(ap,"r")
    lp = f.readlines()
    f.close()
    print("Productos en venta:")
    for e in lp:
        e = e.rstrip("\n")
        dp = e.split(",")
        print(dp[0],": ",dp[1]," - USD ",dp[2])
    np = int(input("Ingrese el número del producto: "))
    cp = int(input("Ingrese la cantidad del producto: "))
    dp = lp[np-1].split(",")
    pp = float(dp[2])
    mc = cp * pp
    print("Monto de la compra: ",mc)
    sc = input("Seguro de comprar S/N?: ")
    sc = sc.upper()
    if sc=="S":
        print("Para concretar la compra ingresa:")
        nc = input("Nombre completo: ")
        rut = input("RUT: ")
        cad_datos_venta = nc+","+rut+","+dp[1]+","+str(cp)+","+str(mc)+"\n"
        f = open(av,"a")
        f.write(cad_datos_venta)
        f.close()
        print("Compra registrada...\n")
    else:
        print("Compra cancelada...\n")

def historial_ventas(av):
    f = open(av,"r")
    lv = f.readlines()
    f.close()
    print("Historial de Ventas")
    print("Nro. Nombre Cliente\t RUT     \t Producto\t\tCantidad Monto Compra")
    nv = 1
    for v in lv:
        v = v.rstrip("\n")
        dv = v.split(",")
        print(nv,". ",dv[0],"\t",dv[1],"\t",dv[2],"\t",dv[3],"\t",dv[4])
        nv += 1
    print()

# Programa principal
# Variables globales   
arch_prod = "datosproductos.csv"
arch_vent = "datosventas.csv"

crea_arch_ventas(arch_vent)
op="X"
while (op!="3"):
    print("Carrito de Compras")
    print("1. Procesar venta\n2. Historial de ventas\n3. Salir")
    op = input("Ingrese la opción: ")
    if op == "1":
        procesar_venta(arch_prod,arch_vent)
    elif op == "2":
        historial_ventas(arch_vent)
    elif op == "3":
        print("Programa terminado...\n\n\n")
        time.sleep(1)
        os.system("cls")