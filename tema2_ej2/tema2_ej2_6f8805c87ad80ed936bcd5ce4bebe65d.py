def amigos(a,b):
    i=1
    div_a= []
    div_b= []
    while i<a or i<b:
        if a%i==0 and i!=a:
            div_a.append(i)
        if b%i==0 and i!=b:
            div_b.append(i)
        i+=1
    z=0
    for t in div_a:
        z+=t
    p=0
    for c in div_b:
        p+=c
    if z==b and p==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    b=int(input("Ingrese b: "))
    print(amigos(a,b))