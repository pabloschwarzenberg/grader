def ADN(string):
    L=['a','c','t','g']
    largo=len(string)
    a=0
    string=string.lower()
    palabra=list(string)
    for i in palabra:
        for j in L:
            if i==j:
                a+=1
    if largo==a:
        return 'secuencia correcta'
    else:
        return 'secuencia incorrecta'
                

string=input()
print(ADN(string))