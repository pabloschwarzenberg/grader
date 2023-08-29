def numero_perfecto(a):
    adiv=[]
    for i in range(1,a):
        if a%i ==0:
            adiv.append(i)
    if sum(adiv)==a:
        return True
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    for i in range(a):
        print(numero_perfecto(i))
           