def buscarTodas(a,b):
    lista = []
    for i in range(len(a)):
        if(a[i]==b):
            lista.append(i)       
    return " ".join([str(_) for _ in lista])

if __name__ == "__main__":
      print(buscarTodas(a,b))
 
           