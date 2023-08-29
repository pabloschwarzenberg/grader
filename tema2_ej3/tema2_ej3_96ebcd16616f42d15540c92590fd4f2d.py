def numero_perfecto(a):
    o = 0
    for e in range(1, a):
        if a % e == 0:
            o = o + e
    if o == a:
        o = True
    else: 
        o = False
    return o

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           