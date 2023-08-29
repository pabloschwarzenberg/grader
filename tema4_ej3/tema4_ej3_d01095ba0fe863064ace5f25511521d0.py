def jerigonzo(string):
    lista_elementos=list(string)
    for i in range(0, (len(lista_elementos))-1):
       puesto=lista_elementos[i]
       segundo=lista_elementos[i+1]
       if puesto=="a" or puesto=="e" or puesto=="i" or puesto=="o" or puesto=="u":
            if segundo=="":
               lista_elementos.join(i+1,"p")
               lista_elementos.join(i+2,puesto)
    texto=""
    return texto.join(lista_elementos)


         