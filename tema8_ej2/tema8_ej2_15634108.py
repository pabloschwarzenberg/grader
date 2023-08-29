def buscarTodas(a,b):
    lista=[]      #Lista de posiciones
    if b in a:
        while b in a:
            palabra_list=list(a)
            posicion=a.find(b)
            lista.append(str(posicion))
            lista.append(" ")
            palabra_list[posicion]="$"
            a="".join(palabra_list)
        lista_string="".join(lista)
        return lista_string
    else:
        return "No se encuentra tal string"

if __name__ == "__main__":
    buscarTodas("tres tristes tigres","t")
    print(buscarTodas("tres tristes tigres","t"))
    
