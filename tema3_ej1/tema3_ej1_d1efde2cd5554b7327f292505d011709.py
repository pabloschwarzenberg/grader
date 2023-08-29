import math
def suma_divisores(a):
    lista =[]
    sumatorio=0
    for i in range(1,int(a/2+1)):
        if a%i == 0:
            sumatorio = sumatorio+i
            lista.append(i)
    if sumatorio == 1:
        b = True
    elif sumatorio != 1:
        b = False
    return sumatorio,b 
          
if __name__ == "__main__":
    a = int(input("num: "))
    print(suma_divisores(a))
    