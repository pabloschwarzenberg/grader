def numero_perfecto(a):
    i=1
    x=[]
    while i<a:
        if a%i==0:
            x.append(i)
        i+=1

    y=0
    for t in x:
        y+=t
    if y==a:
        return True
    elif y!=a:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))