def numero_perfecto(a):
    i = 0
    div = [ ]
    for divisor in range(1,a):
        if a % divisor == 0:
            div.append(divisor)        
            i +=1
    s = sum(div)
    if s == a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           