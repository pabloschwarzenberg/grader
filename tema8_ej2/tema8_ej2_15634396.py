def buscarTodas(frase,letra):
    n=0
    lista=[]
    for letter in frase:
        if letra==letter:
            m=str(n)
            lista.append(m)
            n=n+1
        else:
            n=n+1
    a=''
    b=a.join(lista)
    print(b)

if __name__=="__main__":
  a=input('introduzca frase: ')
  b=input('Introduzca letra: ')
  respuesta=buscarTodas(a,b)


  
    