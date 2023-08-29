import math
def es_primo(x):
    if x==1:
        return False
    else:
        for p in range(2,(round(math.sqrt(x))+1)):
            if (x%p==0)and(p!=x):
                return False
        return True
try:
    x=int(input("INGRESE UN NUMERO: "))
    if x<=0:
        print("EL NUMERO TIENE QUE SER MAYOR QUE CERO")
    else:
        if es_primo(x)==True:
            print("True")
        elif es_primo(x)==False:
            print("False")
except:
    print("INGRESE UN NUMERO NATURAL POR FAVOR")     