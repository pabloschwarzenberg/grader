def son_numeros_amigos(a, b):
    def suma_divisores(numero):
        suma = 0
        for i in range(1, numero):
            if numero % i == 0:
                suma += i
        return suma

    suma_a = suma_divisores(a)
    suma_b = suma_divisores(b)

    if suma_a == b and suma_b == a:
        return True
    else:
        return False
        
 if son_numeros_amigos(numero1, numero2):
    print(f"{numero1} y {numero2} son números amigos")
else:
    print(f"{numero1} y {numero2} no son números amigos")