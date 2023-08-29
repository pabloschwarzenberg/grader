def numero_perfecto(a):
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
def numero_perfecto(numero):
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
    if suma_divisores == numero:
        return True
    else:
        return False

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    if numero_perfecto(numero):
        print(numero, "es un número perfecto.")
    else:
        print(numero, "no es un número perfecto.")
        
        import math

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

if __name__ == "__main__":
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = calcular_area_triangulo(base, altura)
    print("El área del triángulo es:", area)