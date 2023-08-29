def numero_perfecto(a):
    sumas = 0
    for i in range(1,a):
        if (a % i == 0):

            sumas += i
    if a == sumas:
        return True
    else:
        return False       

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           