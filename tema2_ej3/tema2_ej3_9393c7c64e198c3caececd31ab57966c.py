def numero_perfecto(a):
    suma_divisores = 0
    for i in range(1, a):
        if a % i == 0:
            suma_divisores += i

    return suma_divisores == a

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    es_perfecto = numero_perfecto(a)
    
    if es_perfecto:
      print("El número es perfecto.")
    else:
      print("El número no es perfecto.")
           