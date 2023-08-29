def suma_divisores(n):
    i = 1
    numero = n
    suma = 0
    while i < numero:
        if numero%i == 0:
            suma = suma+i
        i = i+1
    if suma == 1:
       print("el numero es primo")
       return suma,True
    elif suma == 0:
       print("el 1 no es un numero primo, pero tampoco compuesto.")
       return suma,False
    elif suma != 1:
       print("el numero no es primo")
       return suma,False
    return suma
   
if __name__ == "__main__":
    a = int(input("ingrese un numero natural: "))
    print("la suma de los divisores del numero es ",suma_divisores(a))           