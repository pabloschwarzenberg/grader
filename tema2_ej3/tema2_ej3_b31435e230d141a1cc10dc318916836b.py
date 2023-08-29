def numero_perfecto(a):
    for i in range(2, a+1):
        b=0
    for j in range(1, (i//2)+1):
        if((i%j)==0):
            b= b+j;
    if(b==i):
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
