def sumadivisores(n):
    j=0
    for i in range(1,n):
        if n%i==0:
            j=j+i
    return j

def amigos(a,b):
    if a==sumadivisores(b) and b==sumadivisores(a):
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese primer número: "))
    b=int(input("Ingrese el segundo número: "))
    
    print(amigos(a,b))