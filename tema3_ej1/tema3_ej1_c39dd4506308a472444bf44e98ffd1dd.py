def esPrimo(x):
    for i in range(2,x):
        if x == 2:
            return True
        elif (x%i) ==0:
            return False
    return True

def suma_divisores(n):
    s=0
    for i in range(n):
        if n!=(i+1):
            resto= n%(i+1)
            if resto==0:
                s=s+(i+1)
    print(s)
    if esPrimo(n) == True:
        print("True")
    else:
        print("False")

x= int(input())
suma_divisores(x)

if __x__ == "__main__":