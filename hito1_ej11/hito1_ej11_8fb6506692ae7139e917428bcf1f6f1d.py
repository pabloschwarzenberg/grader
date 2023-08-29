billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

saldo_20000 = billetes_20000 * 20000
saldo_10000 = billetes_10000 * 10000
saldo_5000 = billetes_5000 * 5000

def imprimir_saldos():
    print("Saldo actual:")
    print("Billetes de 20.000:", billetes_20000)
    print("Billetes de 10.000:", billetes_10000)
    print("Billetes de 5.000:", billetes_5000)

def distribuir_billetes(monto):
    billetes_entregados = {
        20000: 0,
        10000: 0,
        5000: 0
    }

    while monto > 0:
        if monto >= 20000 and billetes_20000 > 0:
            monto -= 20000
            billetes_20000 -= 1
            billetes_entregados[20000] += 1
        elif monto >= 10000 and billetes_10000 > 0:
            monto -= 10000
            billetes_10000 -= 1
            billetes_entregados[10000] += 1
        elif monto >= 5000 and billetes_5000 > 0:
            monto -= 5000
            billetes_5000 -= 1
            billetes_entregados[5000] += 1
        else:
            print("No se pueden entregar los billetes solicitados.")
            break

    if monto == 0:
        print("Retiro exitoso. Billetes entregados:")
        for billete, cantidad in billetes_entregados.items():
            if cantidad > 0:
                print("Billetes de", billete, ":", cantidad)
    else:
        # Si no se pudo entregar el monto exacto, se devuelve el saldo a los billetes disponibles
        billetes_20000 += billetes_entregados[20000]
        billetes_10000 += billetes_entregados[10000]
        billetes_5000 += billetes_entregados[5000]
        print("No se pueden entregar los billetes solicitados.")

    imprimir_saldos()

# Ejecución del programa
print("Bienvenido al cajero automático")
imprimir_saldos()

  while True:
      opcion = input("¿Desea retirar dinero? (s/n): ")

      if opcion.lower() == "s":
          monto = int(input("Ingrese el monto a retirar: "))
          distribuir_billetes(monto)
      elif opcion.lower() == "n":
          print("Gracias por utilizar el cajero automático. ¡Hasta luego!")
          break
      else:
          print("Opción inválida. Por favor, ingrese 's' para retirar dinero o 'n' para salir.")
