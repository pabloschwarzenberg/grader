x=[]
c=[]
j=[]
def buscarTodas(a,b):
    for i in range(len(b)):
        if b[i]==a[0]:
            v=i
        for j in range(len(b)):
            if j<len(a) and j+v<len(b):
                if a[j]==b[j+v]:
                    c=j+v
                    x.append(c)

    k="05913"



if __name__ == "__main__":
  a=str(input("ingrese lo que desea buscar dentro de la frase:"))
  b=str(input("ingrese la frase en la que desea buscar lo anterior:"))
  buscarTodas(a,b)