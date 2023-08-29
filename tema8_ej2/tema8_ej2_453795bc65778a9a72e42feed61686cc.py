def buscarTodas(a,b):
    string=""
    for i in range(len(a)):
        if a[i]==b:
            string=string+str(i)
            string = str(string.split(sep=" ",maxsplit=3))
            #s=" ".join(string)
    return (string)
    pass
if __name__== "__main__":
    print(buscarTodas("tres tristes tigres","t"))
    pass