def buscarTodas(a,b):
    contador=0
    numero=[]
    for i in a:
        if i == b:
            numero.append(str(contador))
        contador+=1
    numero1=" ".join(numero)
    return (numero1)

if __name__ == "__main__":
    pass
           