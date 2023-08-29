def buscarTodas(a,b):
    apariciones=[]
    i=0
    while i<len(a):
        if a.find(b,i) != -1:
            apariciones.append(str(a.find(b,i)))
            i=a.find(b,i)+1
        else:
            i=len(a)
    apariciones=" ".join(apariciones)
    return apariciones

if __name__ == "__main__":
    pass
           