def mcm(a,b,ab):
    ab=1
    h=a*b
    resto = 0
    while(b > 0):
        resto = b
        b = a % b
        a = resto
        j=h/a
    return(j)
if __name__=="__main__":
    a=int(input("Ingrese un numero:"))
    b=int(input("Ingrese un numero:"))
    mcm(a,b,ab)
           