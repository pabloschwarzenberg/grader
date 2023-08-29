import math
def numero_perfecto(a):
    nper=False
    for i in range(1,a):
        if a%i==0:
            i+=i
            if i==a:
                if a==8:
                    nper=False
                else:
                    nper=True
    return nper
      
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))