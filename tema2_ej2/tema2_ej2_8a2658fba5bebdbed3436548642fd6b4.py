def son_amigos(a, b):
    def obtener_divisores(numero):
        div = []
        for i in range(1, numero):
            if numero % i == 0:
                div.append(i)
        return div

    suma_div_a = sum(obtener_divisores(a))
    suma_div_b = sum(obtener_divisores(b))

    return (suma_div_a == b) and (suma_div_b == a)

a = int(input("Ingrese un numero:"))
b = int(input("Ingrese otro numero:"))

if son_amigos(a, b):
    print(f"{a} y {b} son números amigos.")
else:
    print(f"{a} y {b} no son números amigos.")
