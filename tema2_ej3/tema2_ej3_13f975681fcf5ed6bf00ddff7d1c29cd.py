
def numero_perfecto(a):
    cd = 1
    sumadivisores=0
    while (cd < a):
        if (a % cd == 0):
            sumadivisores=cd+sumadivisores
        cd=cd+1
    if(sumadivisores==a):
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           