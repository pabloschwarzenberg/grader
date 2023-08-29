def numero_perfecto(a):
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
def numero_perfecto(numero):
    suma_divisores = sum(divisor for divisor in range(1, numero) if numero % divisor == 0)
    return suma_divisores == numero

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    es_perfecto = numero_perfecto(numero)
    print(es_perfecto)
           