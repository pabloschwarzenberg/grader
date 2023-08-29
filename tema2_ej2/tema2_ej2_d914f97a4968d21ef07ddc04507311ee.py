def son_amigos(a, b):
    def sumar_divisores(num):
        suma = 0
        for i in range(1, num):
            if num % i == 0:
                suma += i
        return suma
    
    suma_a = sumar_divisores(a)
    suma_b = sumar_divisores(b)
    
    if suma_a == b and suma_b == a:
        return True
    else:
        return False

if __name__ == "__main__":
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    resultado = son_amigos(numero1, numero2)
    print("¿Son números amigos?", resultado)
