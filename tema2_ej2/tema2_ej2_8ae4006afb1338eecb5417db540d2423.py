def amigos(l1, l2):
    lamigos = []
    for i in sorted(l1):
        list_temp = [] #Lista temporal
        for j in sorted(l2):
            maxn = max(i, j) #Numero mayor
            minn = min(i, j) #Numero menor
            #Obtengo la unidad del numero mayor
            un = int(str(maxn)[0] + (len(str(maxn)) - 1) * '0')
            #Verifico que el numero menor este en el rango
            #Tambien que el numero mayor sea mayor a 99
            if (minn in list(range(un, maxn)) and maxn > 99):
                #Almaceno en la lista temporal este numero de l2
                #que entra en el rango
                list_temp.append(j)
        #Si existio algun numero en la lista temporal
        if (len(list_temp) > 0):
            #Agrego en la lista a retornar
            #la union entre el numero de l1 y la lista temporal
            lamigos.append([i] + list_temp)
    return lamigos