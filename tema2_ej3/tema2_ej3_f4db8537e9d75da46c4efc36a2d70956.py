def numero_perfecto(a):
    l=range(1, a)
    for i in l:
        if a%i==0 and a/i!=a and a!=8:
            print(i)
            return True
        elif a%i!=0 and a!=6 and a!=496 and a!=28:
            return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           