# completa el código de la función
n1=int(input("Ingrese el primer numero: "))
n2=int(input("Ingrese el segundo numero: "))
def amigos(a,b):
    s1 = 0
    s2 = 0
    for i in range(1,a):
        if a % i == 0:
            s1+=i 
    for j in range(1,b):
        if b % j == 0:
            s2 += j
    if s1 == b and s2 == a:    
        return True
    else:
        return False
print(amigos(n1,n2))