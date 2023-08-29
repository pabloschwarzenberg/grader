def buscarTodas(a,b):
    a=a.upper()
    b=b.upper()
    cantidad=[]
    c=len(a)
    for i in range(c):
        if a[i]==b:
            cantidad.append(str(i))
    cantidad=" ".join(cantidad)
    return cantidad
    pass

if __name__ == "__main__":
    pass
           