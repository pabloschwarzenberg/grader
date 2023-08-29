def jerigonzo(string):
    lista=["a","e","i","o","u"]
    string=str(string)
    lista_string=list(string)
    for i in lista:
        agregado="p"+i
        if i in string:
            m=string.count(i)
            c=1
            p=[]
            n=-1
            while c<=m:   
                n=string.find(i,n+1)
                p.append(n)
                c=c+1
            d=0
            for j in p:
                lista_string.insert(j+1+d,agregado)
                d=d+1
            string="".join(lista_string)
            lista_string=list(string)
    return string
             

if __name__ == "__main__":
    pass
         