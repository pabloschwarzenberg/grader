def numero_perfecto(a):
    l=[]
    s=0
    perfecto = False
    for i in range(1, a):
        if a%i==0:
            l.append(i)
    for j in range(0, len(l)):
        s = s + l[j]
    if s==a:
        perfecto = True
    return perfecto
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           