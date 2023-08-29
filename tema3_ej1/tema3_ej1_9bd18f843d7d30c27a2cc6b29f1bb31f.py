# completa el código de la función
def suma_divisores(a):
    i = 0
    div = [ ]
    for divisor in range(1,a):
        if a % divisor == 0:
            div.append(divisor)
            
            i +=1
    s = sum(div)
    if s == 1:
        lala = (s,True)
        return lala
    else:
        lolo = (s,False)
        return lolo

if __name__ == '__main__':
    num = int(input())
    i = 0
    d = [ ]
    for divisor in range(1,num):
        if num % divisor == 0:
            d.append(divisor)
            i +=1
    sumaD = sum(d)
    print(suma_divisores(num))