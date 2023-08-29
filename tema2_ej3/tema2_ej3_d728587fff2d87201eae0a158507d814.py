def numero_perfecto(a):
    lista_a=[]
    for i in range(1,(a-1)):
        if a%i==0:
            lista_a.append(i)
    if sum(lista_a)==a:
       return True
    else:
        return False
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           