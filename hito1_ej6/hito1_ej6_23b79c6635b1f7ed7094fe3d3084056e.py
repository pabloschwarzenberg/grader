#Ordenar tres números
a =  eval(input("Ingrese el primer numero: "))
b = eval(input("Ingrese el segundo numero: "))
c = eval(input("Ingrese el tercer numero: "))
 
if a>b and b>c: #a>b>c
  print(c, "," ,b, "," ,a)

if a>c and c>b: #a>c>b
  print(b, "," ,c, "," ,a)

if b>a and a>c: #b>a>c
  print(c, "," ,a, "," ,b)

if b>c and c>a: #b>c>a
  print(a, "," ,c, "," ,b)

if c>a and a>b: #c>a>b
  print(b, "," ,a, "," ,c)

if c>b and b>a: #c>b>a
  print(a, "," ,b, "," ,c)

if a == b == c:
    print(a, "," ,b, "," ,c)
    
if a == b and (b > c or a > c): #a,b,c con a y b iguales
    print(c, "," ,b, "," ,a)
    
if a == b and (b < c or a < c):
    print(a, "," ,b, "," ,c)
    
if a == c and (a > b or c > b):
    print(b, "," ,a, "," ,c)
    
if a == c and (a < b or c < b):
    print(a, "," ,c, "," ,b)
    
if b == c and (b > a or c > a):
    print(a, "," ,b, "," ,c)
    
if b == c and (b < a or c < a):
    print(c, "," ,b, "," ,a)

if a == b == c:
    print(a, "," ,b, "," ,c)
    
