#Ordenar tres números
#Entrada
a = int(input("Ingrese un numero : "))
b = int(input("Ingrese un numero : "))
c = int(input("Ingrese un numero : "))


if (b <= a) and (b <= c) and (a <= c):
    orden = b , a , c
    print(",".join([str(b),str(a),str(c)]))
elif (c <= b) and (c <= a) and (b <= a):
    orden = c , b , a
    print(",".join([str(c),str(b),str(a)]))
elif (a <= c) and (a <= b) and (c <= b):
    orden = a , c , b
    print(",".join([str(a),str(c),str(b)]))
elif (a <= c) and (a <= b) and (b <= c):
    orden = a , b , c
    print(",".join([str(a),str(b),str(c)]))
elif (b <= a) and (b <= c) and (c <= a):
    orden = b , c , a
    print(",".join([str(b),str(c),str(a)]))
elif (c <= b) and (c <= a) and (a <= b):
    orden = c , a , b
    print(",".join([str(c),str(a),str(b)]))

    
