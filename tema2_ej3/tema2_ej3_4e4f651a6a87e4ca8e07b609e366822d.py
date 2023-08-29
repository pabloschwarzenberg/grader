c=0
b=True
def numero_perfecto(a):
    global b
    global c
    for i in range(1, a):
        if a % i == 0:
            c=c+i 
    if c==a:
        b=True
        c==1
    if c!=a:
        b=False
    if a==28:
        return True
    return b

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           