def numero_perfecto(a):
    primo = False
    div = []
    for i in range(1, a):
        if a % i == 0:
            div.append(i)

        elif a == 1:
            div = []

#    print(div)
    resultado = 0
    longitud = len(div)
    m=0
    for i in div:
        resultado += i

    if resultado == a:
        return True
    
    else:
        return False
  
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           