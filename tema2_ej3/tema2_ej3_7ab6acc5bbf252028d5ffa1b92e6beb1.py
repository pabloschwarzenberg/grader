def numero_perfecto(a):
    A=0
    i=a
    while i>1:
        if a%i==0:
            c=a/i
            A=A+c
        i=i-1
    if a==A:
        return True
    else: 
        return False


if __name__=="__main__":
    a=int(input("Ingrese a: "))
    A=0
    i=a-1
    while i>1:
        if numero_perfecto(i)==True:
            A=A+i
        else:
            A=A
        i=i-1
    print(A)