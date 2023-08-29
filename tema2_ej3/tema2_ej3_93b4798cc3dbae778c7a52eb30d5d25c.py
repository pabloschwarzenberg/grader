def numero_perfecto(a):
    b=0
    lista=[]
    for i in range(a-1):
        if a%(i+1)==0:
            lista.append(i+1)
    print(lista)
    for i in lista:
        b+=i
    if b==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))