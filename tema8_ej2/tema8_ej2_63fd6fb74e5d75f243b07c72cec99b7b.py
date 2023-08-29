def buscarTodas(a,b):
    string=""
    for i in range(len(a)):
        if a[i]==b:
            string+=""+str(i)
    return (string)
    
print(buscarTodas("tres tristes tigres","t"))
