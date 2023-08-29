def buscarTodas(a,b):
    lista=""
    for i in range(0,len(a)):
        if a[i]==b:
            lista+=str(i)+" "   
        else:
            pass

            
    return lista

if __name__ == "__main__":
    a=input()
    b=input()
    buscar=buscarTodas(a,b)
    print(buscar, end="")


           