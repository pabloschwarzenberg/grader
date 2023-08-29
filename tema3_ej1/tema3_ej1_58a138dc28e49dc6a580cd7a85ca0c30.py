def suma_divisores(a):
    print("calcularemos sus divisores")
    n = []
    for i in range(1,a):
        if a%i == 0:
            n.append(i)
    print("mis divisores son",n)
    n = sum(n)
    print("la suma de mis divisores es:",n)
    if n == 1:
        print("es primo")
        return n, True
    if a == 1:
        print("no es primo")
        return n, False
    
    for i in range(1,a+1):
        if a % 2 == 0:
            print("no es primo")
            return n, False
        elif a % 2 != 0:
            print("es primo")
            return n, True


    
    

    
        


    






if __name__=="__main__":
       
       a = int(input("mencione el numero que va a generar sus divisores: "))
       suma_divisores(a)