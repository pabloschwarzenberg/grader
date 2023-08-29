def numero_perfecto(a):
    suma = sum([i for i in range(1, a) if a % i == 0])
    if suma == a:
        return True
    if suma != a:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           