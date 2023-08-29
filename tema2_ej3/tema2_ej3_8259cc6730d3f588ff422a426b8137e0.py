def numero_perfecto(a):
    divisores=[]
    i=1
    while i<a:
        if a%i==0:
            divisores.append(i)
            i+=1
        else:
            i+=1
    if sum(divisores)==a:
        return True
    else:
        return False
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))