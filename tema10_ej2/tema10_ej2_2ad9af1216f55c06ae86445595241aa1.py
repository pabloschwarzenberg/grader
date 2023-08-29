def levenshtein(palabra1,palabra2):
    diferencias=0
    if len(palabra1)==len(palabra2):
        for i in range(len(palabra1)):
            for j in range(len(palabra2)):
                if i==j:
                    if palabra1[i]!= palabra2[j]:
                        diferencias=diferencias+1
                        
    borrar=False
    if abs(len(palabra1)-len(palabra2)):
        if len(palabra2)>len(palabra1):
            palabra2n=palabra1
            palabra1n=palabra2
        else:
            palabra1n=palabra1
            palabra2n=palabra2
        if len(palabra1n)==len(palabra2n)+1:
            lista1=[]
            cant1=[]
            lista2=[]
            cant2=[]
            for l in palabra1n:
                lista1.append(l)
                suma=0
                for l1 in palabra1n:
                    if l==l1:
                        suma=suma+1
                cant1.append(suma)
            for l in palabra2n:
                lista2.append(l)
                suma=0
                for l1 in palabra2n:
                    if l==l1:
                        suma=suma+1
                cant2.append(suma)

            eliminar=""
            for i in range(len(cant1)):
                for j in range(len(cant2)):
                    if lista1[i] in lista2:
                        if lista1[i]==lista2[j]:
                            if cant1[i]!=cant2[j]:
                                eliminar=lista2[j]
                    else:
                        eliminar=lista1[i]

            prueba=lista1.copy() 
            
            for i in range(len(prueba)):
                letra=(prueba[i])
                if prueba[i]==eliminar:
                    prueba.pop(i)
                    if prueba==lista2:
                        borrar=True
                        break
                    else:
                        prueba.insert(i,letra)

    if palabra1==palabra2:
        return("0D")
    elif diferencias==1:
        return("1S")
    elif borrar==True:
        return("IB")
    else:
        return("+1")