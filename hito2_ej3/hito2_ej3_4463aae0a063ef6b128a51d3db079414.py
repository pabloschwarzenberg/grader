string=input("Ingrese un string:\n")
n=int(input("Ingrese el largo de los substrings únicos: "))
desde=0
particiones=[]
while desde<len(string)-n+1:
    particiones.append(string[desde:desde+n])
    desde+=1
seguir=True
cuantos=[]
while len(particiones)>0 and seguir==True:
    seguir=False
    cuantos.clear()
    for particion in particiones:
        cuanto=particiones.count(particion)
        cuantos.append(cuanto)
        if particiones.count(particion)>1:
            numero=particiones.count(particion)
            a_remover=particion
            for remocion in range(numero):
                particiones.remove(a_remover)
    for cuanto in cuantos:
        if cuanto!=1:
            seguir=True
        


if len(particiones)>0:
    for i in particiones:
        print(i)
else:
    print('ninguna')