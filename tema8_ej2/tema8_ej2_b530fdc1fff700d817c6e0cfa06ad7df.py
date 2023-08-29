def buscarTodas(a,b):
    a=list(a)
    # almacena los indices y las aparaciones
    indices=[]
    aparaciones=0
    # recorrer la palabra
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
    a=buscarTodas(palabra,letrafind)
    print("Las apariciones de la letra", letrafind, "estรกn en los indices:", a)
           