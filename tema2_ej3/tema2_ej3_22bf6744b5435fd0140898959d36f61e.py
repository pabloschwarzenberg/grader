
def numero_perfecto(a):

    x=int(a)
    i=1
    sumatoria=0

    while i>0:
        if (x%i)==0:
            if i==x:
                break
            
            sumatoria=sumatoria+i
            i=i+1
            continue

        else:
            i=i+1
            continue

    if sumatoria==x:
        return True

    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))