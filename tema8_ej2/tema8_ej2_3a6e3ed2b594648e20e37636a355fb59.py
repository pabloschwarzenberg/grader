def buscarTodas(a,b):
    esp = ""
    valor = 0
    for x in a:
        valor_str = str(valor)
        if x == b:
            if esp == "":
                esp += valor_str
            else:
                esp += " "
                esp += valor_str
        valor += 1
    return esp
