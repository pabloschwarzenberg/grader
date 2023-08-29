# completa el código de la función
def amigos(a,b):
    resultadoa=0
    for i in range(1,a+1):
        if a%i==0:
            resultadoa=resultadoa+i
            resultadoaFinal=resultadoa-a      
    resultadob=0
    for i in range(1,b+1):
        if b%i==0:
            resultadob=resultadob+1
            resultadobFinal=resultadoa-b
    if a==resultadobFinal and b==resultadoaFinal:
        return True
    else:
        return False
           