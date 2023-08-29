def buscarTodas(a,b):
    x=[]
    y=0
    while a.find(b,y)!=-1:
        z=a.find(b,y)
        x.append(str(z))
        y=z+1
    alfa=" ".join(x)
    return(alfa)

if __name__ == "__main__":
    palabra=input("Ingrese palabra o frase: ")
    stringb=input("Ingrese string a buscar en palabra: ")
    hola=buscarTodas(palabra,stringb)
    print(hola)
           