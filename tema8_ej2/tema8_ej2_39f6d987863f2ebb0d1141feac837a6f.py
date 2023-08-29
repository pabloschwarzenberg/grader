def buscarTodas(a,b):
    lista= []
    for letra in a:
        lista.append(letra)
    palabra= []
    pal= " "
    cont= 0
    while cont< len(lista):
        if lista[cont]==b:
            palabra.append(pal)
            palabra.append(cont)
        cont= cont + 1
    cont=0
    buscar= " "
    while cont<len(palabra):
        buscar= buscar + str(palabra[cont])
        cont= cont + 1
    return buscar
    
if __name__ == "__main__":
  x= input("palabra:")
  y= input("letra: ")
  z= buscarTodas(x,y)
  print(z)