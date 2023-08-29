def binario(n):
    if n==1:
        return (j for j in "01")
        
    if n!=1:
        return ([i+b for i in "01" for b in binario(n-1)])

def leer(n):
    funcion=binario(n)
    for f in funcion:
        print(f)
    
    
            
            
n=int(input())
leer(n)