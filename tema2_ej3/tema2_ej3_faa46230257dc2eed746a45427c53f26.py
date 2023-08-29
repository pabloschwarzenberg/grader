def numero_perfecto(a):
    suma = 0
    x = 1
    while (x<a):
        if a%x==0:
            suma = suma + x
        x = x+1
    if (a == suma):
        return True
    else:
        return False

a = numero_perfecto(28)
print("Es perfecto?", a)


if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           