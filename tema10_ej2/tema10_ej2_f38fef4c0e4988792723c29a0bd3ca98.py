#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
  if palabra1==palabra2:
        return "0D"
  else:
        m1=len(palabra1)
        m2=len(palabra2)
        if m1>m2:
            i=0
            lista=[]
            while i<m2:
                if palabra1[i]!=palabra2[i]:
                    lista.append(palabra1[i])
                    i+=1
                else:
                    i+=1
            if (len(lista))==0:
                if m1-m2>1:
                    return "+1"
                else:
                    return "IB"
            else:
                c=0
                l1=list(palabra1)
                l2=list(palabra2)
                for a in range(len(l2)):
                    b=l2[a]
                    if l1.count(b)!=l2.count(b):
                       c+=1
                if c>1 or m1-m2>1:
                   return "+1"
                elif c==1:
                   return "IB"

        elif m2>m1:
            j=0
            lista1=[]
            while j<m1:
                if palabra1[j]!=palabra2[j]:
                    lista1.append(palabra2[j])
                    j+=1
                else:
                    j+=1
            if (len(lista1))==0:
                if m2-m1>1:
                    return "+1"
                else:
                    return "IB"
            else:
                c=0
                l1=list(palabra1)
                l2=list(palabra2)
                for a in range(len(l1)):
                    b=l1[a]
                    if l1.count(b)!=l2.count(b):
                       c+=1
                if c>1 or m2-m1>1:
                   return "+1"
                elif c==1:
                   return "IB"
        else:
            k=0
            lista2=[]
            while k<m2:
                if palabra1[k]!=palabra2[k]:
                    lista2.append(palabra1[k])
                    k+=1
                else:
                    k+=1
            if len(lista2)==1:
                    return "1S"
            else:
                return "+1"

if __name__=="__main__":
    palabra1=str(input("Ingrese una palabra: "))
    palabra2=str(input("Ingrese una palabra: "))
    a=levenshtein(palabra1,palabra2)
    print(a)
