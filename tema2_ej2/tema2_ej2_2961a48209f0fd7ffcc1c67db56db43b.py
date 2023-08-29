# completa el código de la función
def amigos(a,b):
    diva=0
    divb=0
    for i in range(1,a):
        if a%i==0:
            diva+=i
            print(i)
    for i in range(1,b):
        if b%i==0:
            divb+=i
    if diva==b:
        return True
    else:
        return False