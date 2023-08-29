#Suma de los N primeros 
def prod_digitos_suma(n):
    #creamos una variable s, donde almacenaremos la suma:
    s=0
    #con un bucle recorremos los números de 0 a n, y se los sumamos a s:
    for i in range(n+1):
        s+=i
    #creamos una variable p, donde almacenaremos el producto:
    p=1
    #convertimos s a una cadena:
    s1=str(s)
    #recorremos dicha cadena con un for:
    for numero in s1:
        #si el numero es 0 nos saltamos la iteracion
        if numero=="0":
            continue
        #myltiplicamos p por los enteros que van tomando el valor caracter, transformandolo antes en entero
        p*=int(numero)
    print("La suma de 1 hasta",n,"es",s)
    print("El producto de sus digitos distintos de 0 es",p)