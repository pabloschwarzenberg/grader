string=input('String= ')
n=int(input('Número entero= '))  
lista=[]
grupo=[]
cont=0
a=''
final = []
while len(string)>=n:
        a=string[0:n]
        lista.append(a)
        string=string[1:]
       
print(lista)
if len(lista)%2 != 1:
    for i in range(len(lista)):            
        for j in range(i+1,len(lista)):
        if lista[i]==lista[j]:
                a = str(lista[i])
                b = str(lista[j])
                lista.remove(a)
                lista.remove(b)
    if lista == []:
        print('ninguna')
    else:
        print(lista)
else:
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i]==lista[j]:
                lista.remove(lista[i])
                lista.remove(lista[j])
    if lista == []:
        print('ninguna')
    else:
        print(lista)      