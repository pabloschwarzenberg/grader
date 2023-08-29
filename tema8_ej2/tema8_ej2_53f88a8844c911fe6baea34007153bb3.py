def buscarTodas(a,b):
    lista_a=list(a)
    string_index=""
    for i in range(0,len(lista_a)):
        if b==lista_a[i]:
            string_index+=" "+str(i)
    lista_string=list(string_index)
    lista_string.remove(" ")
    string="".join(lista_string)
    return string

if __name__=="__main__":
    a=input("ingrese un texto: ")
    b=input("ingrese la letra: ")
    print(buscarTodas(a,b))

           