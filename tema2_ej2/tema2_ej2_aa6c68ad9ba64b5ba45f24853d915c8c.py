# completa el código de la función
def amigos(m,n):
    suma_m=0
    suma_n=0
    for i in range(1,m):
        if m%i==0:
            suma_m+=i
 
    for k in range(1,n):
        if n%k==0:
            suma_n+=k
    
    return suma_m==n and suma_n==m
    if suma_m == n and suma_n == m:
        return True
    else:
        return False   