# completa el código de la función
def amigos (a, b):
    def suma_divisores (n):
        divisores=[]
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
        return suma
    if suma_divisores(a)==b and suma_divisores(b)==a:
        return True
    else:
        return False
           