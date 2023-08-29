def numero_perfecto(n):
    def suma_divisores(n):
        divisores=[]
        m=str("per")
        if n==0:
            print ("Número inválido")
        if n>0:
            for i in range (1,n):
                if (n%i==0):
                    divisores.append(i)
                    i=+1
        if n<0:
            for i in range (n+1,0):
                if (n%i==0):
                    divisores.append(abs(i))
                    i=+1
        suma=0
        for e in divisores:
            suma=suma+e  
        if suma==n:
            n=m
            return True
        if suma != n:
            return False
    nperfectos=[]
    for e in range(1,n):
        if suma_divisores(e)==suma_divisores(6):
            nperfectos.append(e)
            e=+1
        else:
            e=+1
            pass
    suma2=0
    for c in nperfectos:
            suma2=suma2+c
    return suma_divisores(n)

if __name__=="__main__":
    n=int(input("Ingrese n: "))
    print(numero_perfecto(n))
           