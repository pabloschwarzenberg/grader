def numero_perfecto(a):
    i=1
    j=0
    while i<a:
        if a%i==0:
            j=j+i
        i=i+1  
    if j==a:
        return True
    else:
        return False
    
if __name__=="__main__":
    a=int(input("Ingrese a para saber si es un numero perfecto: "))
    print(numero_perfecto(a))
    b=1
    c=0
    while b<a:
        if numero_perfecto(b)==True:
            c=c+b
        b=b+1
    print("La suma de todos los numeros perfectos antes de",a,"es:")    
    print(c)