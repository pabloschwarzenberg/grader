#Conversión de Decimal a Binario


n=int(input(""))
m=str(n)
div=n
lista=[]
lista.append(str(n%2))


while div ==0 or div !=1:
    div=div/2
    div=int(div)
    dig=div%2
    lista.append(str(dig))



    


inv=lista[::-1]

inv="".join(inv)
inv=int(inv)
print("resultado=",inv)