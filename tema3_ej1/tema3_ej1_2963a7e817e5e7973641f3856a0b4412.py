# completa el código de la función
def suma_divisores(a):
    listadivisores=[]
    b=0
    i=1
    a=int(a)
    if type(a)!=int:
        return "Tipo de dato no adecuado"
    if a==1:
        return (0,False)
    while i < ((a//2)+1):
        if a%i==0:
            listadivisores.append(i)
        i+=1
    for x in range(len(listadivisores)) :
        b+=listadivisores[x]
    if b==1:
        return (1,True)
    else:
        return (b,False)