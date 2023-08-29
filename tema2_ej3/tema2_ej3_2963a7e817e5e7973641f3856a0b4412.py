def numero_perfecto(a):
    listadivisores=[]
    b=0
    i=1
    a=int(a)
    if type(a)!=int:
        return "Tipo de dato no compatible"
    if a==1:
        return False
    while i < ((a//2)+1):
        if a%i==0:
            listadivisores.append(i)
        i+=1
    for x in range(len(listadivisores)) :
        b+=listadivisores[x]
    if b==a:
        return True
    else:
        return False
