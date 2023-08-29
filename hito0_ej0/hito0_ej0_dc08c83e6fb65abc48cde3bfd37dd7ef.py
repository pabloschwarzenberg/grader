n=int(input())

def cero(n,num=""):
    x=[]
    if len(num)== n:
        return num
    elif len(num)> n:
        return
    else:
        x.append(cero(n,num+"1"))
        x.append(cero(n,num+"0"))
        return x
x=cero(n)
def cambio(lista):
    if type(lista)!=list:
        print(lista)
        return 
    else:
        for i in lista:
            cambio(i)
cambio(x)
      