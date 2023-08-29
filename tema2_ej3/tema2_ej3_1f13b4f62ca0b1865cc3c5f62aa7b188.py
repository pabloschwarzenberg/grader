
def numero_perfecto(a):

    suma = 0
    perfecto = False
    for i in range(1, a): 

        if (a % i) == 0: 
            suma = suma + i

    else: 
        if suma == a: 
            perfecto = True

    return perfecto

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))

           