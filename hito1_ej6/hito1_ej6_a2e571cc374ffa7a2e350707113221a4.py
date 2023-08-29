#Ordenar tres números
n = int(input())
a = int(input())
b = int(input())
if a>=n>=b :
  print( b, ",", n, ",", a)
if a>=b>=n :
  print( n, ",", b, ",", a)
if n>=a>=b :
  print( b, ",", a, ",", n )
if n>=b>=a :
  print( a, ",", b, ",", n )
if b>=a>=n : 
  print( n, ",", a, ",", b )
if b>=n>=a : 
  print( a, ",", n, ",", b )
      
