def numero_perfecto(a):


    n = []
    for i in range(1,a):
        if a%i == 0: 
            n.append(i)
    print("los divisores de",a,"son",n)
    n = sum(n)
    print("la suma de los divisores es:",n)
    if n == a:
        print("Es numero perfecto")
        return True
    else:
        print("No es numero perfecto")
        return False



if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))