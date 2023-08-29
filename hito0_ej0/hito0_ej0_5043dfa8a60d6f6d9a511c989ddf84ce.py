def interpretar(expresion):
    lista=list(expresion)
    
    if len(lista)==1:
        return lista[0]
    
    else:
        for i in range(1,len(lista),2):
            if lista[i]=='*':
                remp=(int(lista[i-1])* int(lista[i+1]))
                lista.pop(i)
                lista.pop(i)
                lista.pop(i-1)
                lista.insert(i-1,str(remp))
                expresion=''.join(lista)
                return  interpretar(lista)
            elif lista[i]=='/':
                remp=(int(lista[i-1])/ int(lista[i+1]))
                lista.pop(i)
                lista.pop(i)
                lista.pop(i-1)
                lista.insert(i-1,str(remp))
                expresion=''.join(lista)
                return  interpretar(lista)
            else:
                lista[0]=int(lista[0])
                return lista[0] + float(interpretar(lista[2:]))

resultado=interpretar("2*3+5+6*7/9")
print(resultado)