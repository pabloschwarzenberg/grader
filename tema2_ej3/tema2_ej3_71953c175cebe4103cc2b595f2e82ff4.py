def numero_perfecto(a):
    #num=int(input(a))
    num=a
    suma=0
    for i in range(1,num):
        if num%i==0:
            suma=suma+i
    if suma==num:
        resultado=True
    else:
        #suma!=num #DOCENTE: ESTO NO ES CORRECTO
        resultado=False
    return resultado

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           