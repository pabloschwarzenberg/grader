# completa el código de la función
def suma_divisores(a):
    suma = 0
    for i in range(1, a):
        if a % i == 0:
            suma = suma + i
    if suma == 1:
        v = True
    else:
        v = False
    return suma,v
   
if __name__ == "__main__":
    a = int(input("Ingresa un numero: "))
    z = suma_divisores(a)
    print(z)
    
