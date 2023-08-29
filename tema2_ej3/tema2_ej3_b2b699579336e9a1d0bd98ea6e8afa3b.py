def numero_perfecto(a):
    sumadivisores = 0
    for i in range(1,a):
        if a%i == 0:
            sumadivisores = sumadivisores + i
    if sumadivisores == a:
        return (True)
    else:
        return (False)

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           