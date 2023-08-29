def jerigonzo(string):
    lista = []
    texto = string
    for i in texto:
            lista.append(i)
            if i =="a":
                lista.append("p")
                lista.append(i)
            if i =="e":
                lista.append("p")
                lista.append(i)
            if i =="i":
                lista.append("p")
                lista.append(i)
            if i =="o":
                lista.append("p")
                lista.append(i)
            if i =="u":
                lista.append("p")
                lista.append(i)
    string =""
    for i in lista:
        string += i
    return string