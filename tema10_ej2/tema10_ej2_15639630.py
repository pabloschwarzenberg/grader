#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguale

def levenshtein(a,b):
    h=0
    i=0
    if a==b:
        return '0D'
    if abs(len(a)-len(b))>1:
        return '+1'

    if len(a)==len(b):
        i+=1
        print('caca')
        return '+1'
    if len (b)> len(a):
        i +=1
        j = 0
        for t in range(len(a)-1):
            if a[t] != b[t]:
                j=j+1

        if j>1:
            return '+1'
        if j==1:
            h = h+1
    if len (a)> len(b):
        i +=1
        j = 0
        for t in range(len(a)-1):
            if a[t] != b[t]:
                j=j+1

        if j>1:

            return '+1'

        if j==1:
            h = h+1
    if h==1 and i==1:
        return '+1'

    if h==1 and i==0:
        return '1S'
    if h==0 and i==1:
        return 'IB'
    print(h,i)
if __name__=="__main__":
  a=input('palabra 1?')
  b=input('palabra 2?')
  levenshtein(a,b)
