#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
def resolver(todas_las_opciones):
    parcial=[]
    soluciones=[]
    resolver_rec(parcial,soluciones,todas_las_opciones)
    return soluciones
def resolver_rec(parcial,soluciones,posibles_opciones,n):
    cantidad_max= n 
    if len(parcial)==cantidad_max:
        if validar_solucion(parcial):
            lista_copia=parcial.copy()
            soluciones.append(lista_copia)
    else:
        i=0
        while i<len(posibles_opciones):
            opcion_a_agregar=posibles_opciones[i]
            nuevas_posibles=posibles_opciones[i+1:]
            parcial.append(opcion_a_agregar)
            resolver_rec(parcial,soluciones,nuevas_posibles,n)
            parcial.pop()
            i+=1
def validar_solucion(solucion_parcial):
    
    
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
print("0000")
           