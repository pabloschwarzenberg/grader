def buscarTodas(a,b):
    lista =[]
    separacion=""
    d = " "
    count=0
    for i in a:
      if i == b:
        c = str(count)
        separacion = separacion + c + d   
      int(count)
      count+=1
    final = separacion[:-1]    
    return final
    pass 


if __name__ == "__main__":
    a = input()
    b = input()
    print(buscarTodas(a,b))
    pass
           