def suma_divisores(a):
    x = 0
    for i in range(1,a):
        if a%i ==0:
            x= x + i
    d = True
    if a==2:
        d=True
    else:
        if a<=1:
             d = False
        else:
             for i in range(2,a):
                if a%i==0:
                     d=False
    return(x,d)

if __name__ == "__main__": suma_divisores(a)  