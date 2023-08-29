#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    pass
    if len(palabra1)==len(palabra2):
        p=0
        for i in range(len(palabra1)):
            if palabra1[i]==palabra2[i]:
                p+=1
            if p==len(palabra1):
                return "0D"
        if p==(len(palabra1)-1):
            return "1S"
    elif len(palabra1)>len(palabra2):
         d=len(palabra1)-len(palabra2)
         if d>=2:
             return "+1"
         else:
             p=0
             for i in range(len(palabra2)):
                 if palabra2[i] in palabra1:
                     p+=1
                     if p==len(palabra2):
                         return "IB"
             if p<len(palabra2):
                  return "+1"
    elif len(palabra1)<len(palabra2):
         d=len(palabra2)-len(palabra1)
         if d>=2:
             return "+1"
         else:
             p=0
             for i in range(len(palabra1)):
                 if palabra1[i] in palabra2:
                     p+=1
                     if p==len(palabra1):
                         return "IB"
             if p<len(palabra2):
                  return "+1"

if __name__=="__main__":
    pass
    while True:
        A=input("Ingrese palabra 1: ")
        B=input("Ingrese palabra 2: ")
        print(levenshtein(A,B))