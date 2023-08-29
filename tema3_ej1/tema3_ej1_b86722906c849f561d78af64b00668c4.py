# completa el código de la función

def suma_divisores(a):
    lista = []
    for i in range(1,a):
        if a%i == 0:
          lista.append(i)
    suma = 0
    for i in lista:
        suma += i
    if suma == 1:
        return suma,True
    else:
        return suma,False

if __name__ == "__main__":
    n = int(input("Ingrese un número: "))
    print(suma_divisores(n))
           