def buscarTodas(a,b):
    indice=0
    ret=""
    for i in a:
        if i==b:
            ret+=str(indice)+" "

        indice+=1
    ret= ret.split(" ")
    ret.pop(len(ret)-1)
    ret=" ".join(ret)
    return ret
    
if __name__ == "__main__":
    a=input("ingrese palabra en la que buscar")
    b=input("ingrese la palabra que buscar")
    
    print(buscarTodas(a,b))
           