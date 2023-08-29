def suma_divisores(a):
    div=[]
    for i in range(1,a):
        if a%i==0:
            div.append(i)
    if sum(div)==1 and a!=1:
        return sum(div),True
    else:
        return sum(div),False

if __name__=="__main__":
    print("Ingrese un número para sumar sus divisores y ver si es primo.")
    num=int(input("Número: "))
    print(suma_divisores(num))
