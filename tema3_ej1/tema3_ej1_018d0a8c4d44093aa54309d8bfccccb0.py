# completa el código de la función
def suma_divisores(a):
    s=0
    a=int(a)
    i=1
    while i<a:
        if a/i==a//i:
            s=i+s
        i=i+1
    if s==1:
        n= True 
    if s!=1:
        s=s
        n= False
    return s,n

if __name__ == "__main__":
    print(suma_divisores())
