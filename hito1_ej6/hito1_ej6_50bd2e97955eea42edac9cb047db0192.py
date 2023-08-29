#Ordenar tres números

a = eval(input("escriba el primer numero:"))
b = eval(input("escriba el segundo numero:"))
c = eval(input("escriba el tercer numero:"))

if a < b < c:

    print (a , "," , b , "," , c)

elif b < a < c:

    print (b , "," , a , "," , c)

elif c < a < b:

    print (c , "," , a , "," , b)

elif a < c < b:

    print (a , "," , c , "," , b)

elif b < c < a:

    print (b , "," , c , "," , a)

elif c < b <a:

    print (c , "," , b , "," , a)

elif a == b < c:

    print (a , "," , b , "," , c)

elif a < b == c:

    print (a , "," , b , "," , c)

elif a == b > c:

    print (c , "," , a , "," , b)

elif a == c > b:

    print (b , "," , c , "," , a)

elif a == c < b:

    print (a , "," , c , "," , b)
    
elif a == c == b:

    print (b , "," , c , "," , a)
