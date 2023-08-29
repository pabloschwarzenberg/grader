def numero_perfecto(a):
    p=0
    for x in range(1,a):
        if ((a%x)==0):
            p+=x
    if a==p:
        return True
    else:
        return False
if __name__ == "__main__":
    a = int(input("Ingrese a: "))
    print(numero_perfecto(a))