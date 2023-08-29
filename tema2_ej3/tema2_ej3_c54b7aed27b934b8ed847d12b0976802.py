def numero_perfecto(a):
    div = 1
    suma = 0
    vf = a
    while div < a:
        if a % div == 0:
            suma = suma + div
        div = div + 1
    if suma == a:
        vf=True
    else:
        vf=False
    return (vf)
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           