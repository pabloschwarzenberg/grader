def numero_perfecto(n):
        inicio=1
        s=0
        while inicio!=n:
            if n%inicio==0:
                s=s+inicio
            inicio=inicio+1
        if s==n:
            return True
        else:
            return False
if __name__=="__main__":
    n=int(input("Ingrese el numero: "))
    print(numero_perfecto(n))
           