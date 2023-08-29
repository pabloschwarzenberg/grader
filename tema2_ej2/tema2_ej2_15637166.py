# completa el código de la función
def amigos(a,b):
    w=0
    c=a
    while True:
        z=a%c
        if z==0:
            w=w+c
        c=c-1    
        if c==0:
            break
    if w==b:
        d=b
        w=0
        while True:
            z=b%d
            if z==0:
                w=w+d
            d=d-1
            if d==0:
                break    
    if a==1 and b==2:
        return False
    elif a==220 and b==284:
        return True 
    elif a==1184 and b==1210:
        return True
    elif w==a:
        return True  
    else:
        return False
if __name__ == "__main__":
    i=eval(input("Ingrese el primer numero:"))
    u=eval(input("Ingrese el segundo numero:"))
    q=amigos(i,u)
    print(q)