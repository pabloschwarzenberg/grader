# completa el código de la función
def suma_divisores(a):
    suma = 0
    for i in range(1, a+1):
        if a % i == 0:
            suma += i
    return suma
def es_primo(a):
    if a < 2:
        return False
    for i in range(2, int(a**0.5)+ 1):
        if a % i ==0:
            return False
    return True
 
if __name__ == "__main__":
    a = int(input("ingrese numero: "))
    r = suma_divisores(a)
    if es_primo(r):
        print("La suma de los divisores son", r, "y es primo")
    else:
        print("la suma de los divisores son", r, "no es primo")

           