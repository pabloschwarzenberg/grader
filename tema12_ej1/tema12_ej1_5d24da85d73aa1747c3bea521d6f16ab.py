def numeros_binarios(n,solucion_parcial,soluciones):

    if len(solucion_parcial) == n:
        s = "".join(solucion_parcial)

        if s not in soluciones:
            soluciones.append(s)
        return
    else:
        for opcion in ["0","1"]:
            solucion_parcial.append(opcion)
            numeros_binarios(n,solucion_parcial,soluciones)
            solucion_parcial.pop()

    return soluciones


for i in numeros_binarios(int(input()),[],[]):
    print(i)
           