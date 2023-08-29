def numero_perfecto(a):
    i=1
    s=0
    while i!=a:
        if a%i==0:
            s=s+i
        i+=1
    if s==a:
        return True
    else:
        return False
 
if __name__=="__main__":
    a=eval(input("Ingrese a: "))
    print(numero_perfecto(a))
           