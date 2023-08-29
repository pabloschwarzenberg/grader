
def wEsTSidE(string,n):
    string = list(string)

    j = n
    
    lista = [q for q in range(len(string))]
    lista2 =[]
    lista3 = []
    listafinal = []

    for numero in lista:
        x = string[numero:j]
        j+=1
        lista2.append(x)


    for elem in lista2:
        if len(elem) == n:
            elem = "".join(elem)
            lista3.append(elem)
    
    for e in lista3:
        x = lista3.count(e)
        if x < 2:
            listafinal.append(e)

    return listafinal 


string = str(input("Subsecuencias de ADN: "))
n = int(input("numero : "))
y = wEsTSidE(string,n)

if len(y) != 0:
    for i in y:
        print(i)
else:
    print('ninguna')