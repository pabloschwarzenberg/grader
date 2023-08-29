def numero_perfecto(a):
    b=0
    j=0
    while(b<a):
        b=b+1
        if (a == b):
            break
        if(a%b==0):
            j=j+b
    if(a==j):
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           