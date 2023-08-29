def numero_perfecto(a):
    dvsr=[]
    for i in range(1,a):
        if a%i==0:
            dvsr.append(i)
    b=0
    for i in range(0,len(dvsr)):
        b=b+dvsr[i]
    if b==a:
        return True 
    else:    
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           