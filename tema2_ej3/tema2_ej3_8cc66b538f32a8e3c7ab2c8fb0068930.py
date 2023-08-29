def numero_perfecto(a):
    b=1
    c=0
    while b<a:
        if a%b==0:
            c=c+b
        else:
            c=c
        b=b+1
    if c==a:
        return True
    else:
        return False
    
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           
