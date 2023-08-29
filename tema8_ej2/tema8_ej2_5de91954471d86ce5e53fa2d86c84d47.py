def buscarTodas(a,b):
    string=''
    for x in range(len(a)):
        if a[x]==b:
            string+=str(x)+' '
    return string[:-1]

if __name__ == "__main__":
    pass
           