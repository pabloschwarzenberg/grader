def suma_divisores(a):
    lista=[]
    for i in range(a):
        if a%(i+1)==0 and a!=i+1:
            lista.append(i+1)
    suma=0
    for i in lista:
        suma+=i
    print(suma)
    if suma==1:
        return suma, True
    else:
        return suma, False
if __name__ == "__main__":
    numero=int(input("numero:"))
    print(suma_divisores(numero))