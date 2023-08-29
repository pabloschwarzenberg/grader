def buscarTodas(a,b):
    a=list(a)
    indices=[]
    aparaciones=0
    largo_palabra=len(a)
    conta_min=0
    while conta_min < largo_palabra:
        if b == a[conta_min]:
            indices.append(conta_min)
            aparaciones+=1
        conta_min=conta_min+1
    index_f=' '.join(str(e) for e in indices)
    return index_f

if __name__=="__main__":
    palabra=input("Ingrese una palabra: ")
    letrafind=input("Ingrese la letra que quiere buscar: ")
    buscarTodas(palabra,letrafind)
    print("Las apariciones de la letra", letrafind, "están en los indices:", buscarTodas(palabra,letrafind))