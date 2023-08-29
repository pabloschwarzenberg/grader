def ocultar_letras(palabra,cantidad):
    string=palabra
    lista=[str(x) for x in string]
    a=len(lista)
    a1=a-1
    b=0
    for a in lista:
        while b<cantidad:
            lista[a1]=("_")
            break
        b+=1
        a1-=2
    palabra1=''.join(lista)
    return(palabra1)
    

def revisar_letra(palabra_secreta,palabra,letra):
    return palabra

if __name__ == "__main__":
    pass
         