def numero_perfecto(a):
    la=0
    for i in range(1,a) :
        if a%i==0:
            la=la+i
    if la==a:
        return True
    else:
        return False
    
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))    

