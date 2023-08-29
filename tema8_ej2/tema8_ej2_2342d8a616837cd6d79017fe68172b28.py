resultados=""
resultados_l=""
def buscarTodas(a,b):
    a_l=list(a)
    resultados=""
    resultados_l=list(resultados)
    q=0
    for n in a_l:
        if n==b:
            q_str=str(q)
            resultados_l.append(q_str)
            resultados_l.append(" ")
            q=q+1
        else:
            q=q+1
    resultados="".join(resultados_l)
    return resultados
print(resultados)

if __name__ == "__main__":
    pass
           