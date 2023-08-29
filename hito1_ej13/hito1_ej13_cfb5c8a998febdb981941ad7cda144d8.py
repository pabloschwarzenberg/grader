n = int(input("Ingrese numero:"))
divisores=[]
primos = []
for i in range(1,n):
    x= n%i
    if x==0:
        divisor= i
        divisores.append(divisor)
def es_primo(n):
    if n==1:
        return False
    for i in range(2,n):
        d= n%i
        if d==0:
            x=i
            if x>1:
                return False
    for i in range(2,n+1):
        d=n%i
        if d==0:
            x=i
            if x==i:
                return True
for i in divisores:
    p = es_primo(i)
    if p == True:
        primos.append(i)
print(primos)
