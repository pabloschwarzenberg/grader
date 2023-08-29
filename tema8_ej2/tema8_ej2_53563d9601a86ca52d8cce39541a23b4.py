def buscarTodas(a,b):
    string=""
    for i in range(len(a)):
        if a[i]==b:
            string+=" "+str(i)
    return (string)
    pass
if __name__ == "__main__":
    print(buscarTodas("tres tristes tigres","t"))
    pass