def numero_perfecto(a):
    k = 0
    for numero in range(1,a):
        if a % numero == 0:
            k += numero
    if k == a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    suma = 0
    for numero in range(1,a):
        if numero_perfecto(numero):
            suma += numero

    print("La suma de los números perfectos hasta", a, "es", suma)
           