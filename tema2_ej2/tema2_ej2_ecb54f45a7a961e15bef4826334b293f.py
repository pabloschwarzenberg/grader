# completa el código de la función
def amigos(a,b):
    divisor_1=2
    divisor_2=2
    n_1=0
    n_2=0
    while divisor_1<=a:
        if a%divisor_1==0:
             n_1+=divisor_1
        divisor_1+=1
    while divisor_2<=b:
        if b%divisor_2==0:
             n_2+=divisor_2
        divisor_2+=1
    if n_1==n_2 and a!=b:
        print(n_1,n_2)
        print("True")
        return True
    else:
        print(n_1, n_2)
        print("False")
        return False

           