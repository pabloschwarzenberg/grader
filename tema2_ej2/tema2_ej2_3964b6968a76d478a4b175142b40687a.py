# completa el código de la función
def amigos(a,b):
    divisorA=[]
    for i in range(1,a):
        if a%i==0:
            i=divisorA.append(i)
    divisorB=[]
    for i in range(1,b):
        if b%i==0:
            i=divisorB.append(i)

    print("divisores de a=", divisorA, "\n"+"divisores de b=", divisorB)  