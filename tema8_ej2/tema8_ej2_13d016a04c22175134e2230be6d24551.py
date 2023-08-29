def buscarTodas(a,b):
        listabusqueda=list(a)
        cont=0
        listafinal=[]
        while cont<len(listabusqueda):
            if listabusqueda[cont]==b:
                listafinal.append(str(cont))
                listafinal.append(" ")
            cont+=1
        listafinal.pop(len(listafinal)-1)
        listafinal="".join(listafinal)
        return listafinal