def buscarTodas(a,b):
    string=""
    for i in range(len(a)):
        if (a[i]==b):
            string+=str(i)+" "
    return string.strip(" ")
if __name__ == "_main_":
    print(buscarTodas("tres tristes tigres","t"))
    pass
           