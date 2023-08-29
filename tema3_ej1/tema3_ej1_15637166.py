#SUMA DE LOS DIVISORES DE UN NUMERO
def suma_divisores(a):
    w=0
    c=a-1
    while True:
        
        if c<=0:
            break
        z=a%c
        if z==0:
            w=w+c
        c=c-1  
        
    if w==1:
        return w,True
    else:
        return w,False
if __name__ == "__main__":
    i=eval(input("Ingrese el primer numero:"))
    q=suma_divisores(i)
    print(w,q)       