def numero_perfecto(a):       # PARTE 1
    suma=0
    if a==1:
        print("  Se cumple que", a, "es un número perfecto.")
        return True
    elif a!=1:
        for i in range(1, a-1):
            if a%i==0:
                suma = suma + i
        if suma==a:
            print("  Se cumple que", a, "es un número perfecto.")
            return True
        else:
            print("  No se cumple que", a, "es un número perfecto.")
            return False
    
    


if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           