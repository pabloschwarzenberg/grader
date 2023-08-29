def rot13(texto):
    listaMayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM";
    listaMinus = "abcdefghijklmnopqrstuvwxyzabcdefghijklm";
    resultado= ""
    for i in texto:
        if i in listaMayus:
           resultado = resultado+listaMayus[listaMayus.find(i)+13]
        elif i in listaMinus:
            resultado = resultado+listaMinus[listaMinus.find(i)+13]
        else:
            resultado = resultado+i
    return resultado
        
