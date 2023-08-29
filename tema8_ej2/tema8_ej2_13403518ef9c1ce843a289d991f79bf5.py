def buscarTodas(a,b):
    indices  = []
    indice = 0
    strindices = ""
    for i in a:
       if i ==b:
           indices.append(indice)
       indice+=1
    for i in indices:
       strindices+=str(i)
       strindices+=" "
    return strindices

if __name__ == "__main__":
    string1 = input("Que string quieres revisar?")
    string2 = input("Que letra quieres buscar?")
    resultado =(buscarTodas(string1,string2))
    print (resultado)

