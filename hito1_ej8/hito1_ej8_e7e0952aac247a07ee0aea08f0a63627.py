#Descomponer un número
n = int(input("Ingrese un numero de hasta 4 digitos:"))

if n < 10:
    print(n,"U")
    
if n >= 10 and n <= 99:
    d = n//10
    u = n%10
    print(d,"D", "+", u,"U")

if n >= 100 and n <= 999:
    c = n//100
    x = n%100
    y = x//10
    z = x%10
    print(c,"C", "+", y,"D", "+", z,"U")

if n >= 1000 and n<= 9999:
    a = n//1000
    b = n%1000
    e = b//100
    q = b%100
    p = q//10
    r = q%10
    print(a,"M", "+", e,"C", "+", p,"D", "+", r,"U")

