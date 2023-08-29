# completa el código de la función
def amigos(a,b):
  return
    print("DIVISORES")
    numero = int(input("Escriba un número entero mayor que cero: "))

    if numero <= 0:
        print("¡Le he pedido un número entero mayor que cero!")
    else:
        print(f"Los divisores de {numero} son ", end="")
        for i in range(1, numero // 2 + 1):
            if numero % i == 0:
                print(i, end=" ")
        print(f"{numero} ")
