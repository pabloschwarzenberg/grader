# completa el código de la función
__author__ = 'Damian'
def amigos(x, y):
    sum1=0
    sum2=0
    for i in range(1, x):
        if x%i==0:
            sum1 = sum1 + i
    for i in range(1, y):
        if y%i==0:
            sum2 = sum2 + i
    print("")
    if sum1==y and sum2==x:
        print("  Se cumple que", x, "y", y, "son números amigos.")
        return True
    else:
        print("  Lo siento,", x, "y", y, "no son números amigos.")
        return False