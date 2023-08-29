nro = int(input())

def binarios(binario=[],historial=[],soluciones=[]):
    if len(binario) == nro:

        #soluciones.append(binario)
        #a = str(binario)
        soluciones.append("".join(binario))
        #print("".join(binario))
        return True
    if len(binario) > nro:
        return False

    if binario in soluciones:
        return False

    for i in range(0, 2):
        c_binario = binario[:]
        c_binario.append(str(i))
        c_historial = historial
        c_historial.append(binario)
        c_soluciones = soluciones

        binarios(c_binario, c_historial,c_soluciones)
    return soluciones

for i in binarios():
    print(i)