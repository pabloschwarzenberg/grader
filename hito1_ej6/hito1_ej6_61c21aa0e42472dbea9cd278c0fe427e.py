#Ordenar tres números
a = int (input ("Ingrese el primer numero: "))
print(a)
b = int (input ("Ingrese el segundo numero: "))
print(b)
c = int (input ("Ingrese el tercer numero: "))
print(c)
if a <= b and b <= c:
    print(str( a ),",", str( b ),",", str( c )) 
elif a <= c and c <= b:
    print(str( a ),",", str( c ),",", str( b ))
elif b <= a and a <= c:
    print(str( b ),",", str( a ),",", str( c ))  
elif b <= c and c <= a:
    print(str( b ),",", str( c ),",", str( a ))   
elif c <= a and a <= b:
    print(str( c ),",", str( a ),",", str( b ))
elif c <= b and b <= a:
    print(str( c ),",",str( b ),",",str( a ))


    
  
