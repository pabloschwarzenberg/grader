def numero_perfecto(a):
    divisores = [1]
    for i in range(2, a):
            if a % i == 0:
                divisores.append(i)
                z=sum(divisores)
                if z == a:
                    return True

    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           