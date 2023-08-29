def numero_perfecto(a):
    n = []
    x = 0
    b = 0
    for i in range(1,a):
        if a%i == 0:
            n.append(i)
    for i in n:
        x+=n[b]
        b+=1

    if x == a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    numero_perfecto(a)
           