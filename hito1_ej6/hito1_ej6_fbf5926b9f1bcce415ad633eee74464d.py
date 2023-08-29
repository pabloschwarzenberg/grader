#Ordenar tres números
a = 0
b = 0
c = 0

print("ingrese el primer numero:")
a = int(input())

print("ingrese el segundo numero:")
b =int(input())

print("ingrese el tercer numero:")
c = int(input())

if ( a < b and b < c ):
    print ( a,",",b,",",c )
elif(b < a and  a < c):
   print ( b,",",a,",",c )
elif(c > a and a < b ):
    print ( a,",",c,",",b )
elif(c < a and b < a ):
    print ( c,",",b,",",a )
elif(c < a and b < c ):
    print ( b,",",c,",",a )
elif(b < a and c > a ):
    print ( c,",",b,",",a )
elif(b > a and c < a ) :
    print ( c,",",a,",",b )
elif(a == b and c > a ):
    print ( a,",",b,",",c )
elif(a == c and b > a ):
    print ( a,",",c,",",b )
elif(b == c and b > a ):
    print ( a,",",c,",",b )
elif(a == b and c < a ):
    print ( c,",",b,",",a )
elif(a == c and b < a ):
    print ( b,",",c,",",a )
elif(b == c and b < a ):
    print ( b,",",c,",",a )