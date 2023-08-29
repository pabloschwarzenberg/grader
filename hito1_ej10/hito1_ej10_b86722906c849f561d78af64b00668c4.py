saldo_cajero = 1000000
saldo_cuenta = 100000

print("\n")

print("Bienvenido a Santander")
print("\n")
usuario = int(input("Ingrese usuario: "))

if usuario == 10334151:
    clave = int(input("Ingrese clave: "))
    if usuario != 10334151:
        usuario = int(input("Ingrese usuario: "))
    
    
if clave == 1803:
    print("Clave válida!")
    monto = int(input("Ingrese monto a retirar: "))
else:
    max_index = 2
    counter = 0
    
    while counter <= max_index:
        clave = int(input("Clave inválida, intente de nuevo: "))
        continue
        counter = counter + 1
        if counter == 3:
              print("Tarjeta bloqueada")
              break

if monto > 100000:
    print("Monto no permitido")
    monto = int(input("Seleccione otro monto: "))
else:
    saldo_cuenta = saldo_cuenta - monto
    saldo_cajero = saldo_cajero - monto
    print("Saldo cuenta =", saldo_cuenta)
    print("Saldo cajero =", saldo_cajero)