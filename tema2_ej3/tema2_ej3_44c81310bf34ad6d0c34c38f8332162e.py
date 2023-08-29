def numero_perfecto(num):
    suma=0
    for i in range(1,num):
        if num%i==0:
            suma+=i
    return suma==num
if __name__=="__main__":
    num=int(input('ingresa un numero:'))
    print(numero_perfecto(num))