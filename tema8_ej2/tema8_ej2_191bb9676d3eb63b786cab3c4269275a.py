def buscarTodas(a,b):
    l=[]
    lista=list(a)
    largo=len(lista)
    for i in range (0,largo):
        if lista[i]==b:
           l.append(str(i))
    string=" ".join(l)
           
    return string       

if __name__ == "__main__":
  a=input("Escriba una frase ")
  b=input("Escriba la letra que desea buscar ") 
  print(buscarTodas(a,b))
       
           