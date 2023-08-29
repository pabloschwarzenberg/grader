# completa el código de la función
def son_amigos(a, b):
    def obtener_divisores(n):
        div = []
        for i in range(1, n):
            if n % i == 0:
                div.append(i)
        return div

    suma_div_a = sum(obtener_divisores(a))
    suma_div_b = sum(obtener_divisores(b))

    if suma_div_a == b and suma_div_b == a:
        return True
    else:
        return False
        
        num1 = 220
num2 = 284

if son_amigos(num1, num2):
    print(f"{num1} y {num2} son números amigos.")
else:
    print(f"{num1} y {num2} no son números amigos.")


           