def binarios(binario,lista_binarios=[]):
    if binario not in lista_binarios:
        lista_binarios.append(binario)
    if len(lista_binarios) == x:
        return lista_binarios
    for elemento in range(len(binario)):
        l = list(binario)
        if binario[elemento] == "0":
            caca = l.pop(elemento)
            l.insert(elemento,"1")
            if "".join(l) not in lista_binarios:
                lista_binarios.append("".join(l))
                b = "".join(l)
                binarios(b,lista_binarios)
    return lista_binarios

        
n = int(input())
x = 2**n
binario1 = "0"*n
resultado = binarios(binario1)
for e in resultado:
    print(e)