# completa el código de la función
#Esta función retornará tanto la suma de los divisores del numero, como el hecho de si el número es primo o no (Entre los divisores del numero no se considerará al mismo numero)
def suma_divisores(a):
    if a==1:
        return (0,False)
    else:
        i=1
        divisores=[]
        while i<a:
            if a%i==0:
                divisores.append(i)
                i=i+1
            else:
                i=i+1
        suma=0
        l=0
        while l<len(divisores):
            divisor=int(divisores[l])
            suma=suma + divisor
            l=l+1
        if suma==1:
            return (suma,True)
        else:
            return (suma,False)
           