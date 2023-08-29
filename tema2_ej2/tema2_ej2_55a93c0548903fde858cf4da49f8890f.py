# completa el código de la función
def amigos(a,b):
    v = range(1,a)
    v2 = range(1,b)
    divi = 0
    for i in v:
        if a % i == 0:
            divi += i
    print(divi)
    div = 0
    for j in v2:
        if b % j == 0:
            div += j
    print(div)
    if a == div and b == divi:
        return True
    else:
        return False
print(amigos(220,284))

           