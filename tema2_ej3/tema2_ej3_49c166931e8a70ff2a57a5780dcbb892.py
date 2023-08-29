def divisores(n):
    f=n
    div=[]
    while n!=0:
        d=f%n
        n=n-1
        if d==0:
            div.append(n+1)
    return div
def numero_perfecto(n):
    i=1
    s=0
    while i< len(divisores(n)):
        s=s+divisores(n)[i]
        i=i+1
    if s==n:
        return True
    else:
        return False
if __name__ == "__main__":
    n=input("ingrese un numero")
    n=float(n)
    i=0
    s=0
    while i<n:
        if numero_perfecto(i):
            s=s+i
            i=i+1
    print("la suma de los numeros perfectos menores que",n,"es",s)

           