def buscarTodas(a,b):
    posiciones=[]
    
    for i in range(len(a)):
        if a[i]==b:
            i=str(i)
            posiciones.append(i)

    return " ".join(posiciones)

if __name__ == "__main__":
  a=input("Ingrese una frase: ")
  b=input("Ingrese una letra: ")  
  print(buscarTodas(a,b))
           