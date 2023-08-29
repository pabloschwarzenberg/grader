def numero_perfecto(a):
    c=1
    d=0
    for i in range(a-1) :
        if a%c==0 :
            d=d+c
        c+=1
     
    if d==a:    
        return True
    else :
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           