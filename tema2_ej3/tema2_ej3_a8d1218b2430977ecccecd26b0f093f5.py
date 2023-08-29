def numero_perfecto(a):
    suma_div = 0
    for i in range(1,a):
        if a % i == 0:
            suma_div = suma_div + i
    #print(suma_div)
    if a == suma_div:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(f"{numero_perfecto(a)}")
           