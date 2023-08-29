# completa el código de la función
def suma_divisores(a):
    s=0
    d=1
    for d in range(1,a):
        if(a%d==0):
            s=s+d
    if(s==1):
        return (s,True)
    else:
        return (s,False)
    
    
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(suma_divisores(a))
   