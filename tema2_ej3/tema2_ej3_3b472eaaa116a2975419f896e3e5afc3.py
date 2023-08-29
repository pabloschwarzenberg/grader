def numero_perfecto(a):
    div=[]
    for i in range(1,a):
        if a%i==0:
            div.append(i)
        if sum(div)==a:
            return True
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           
           