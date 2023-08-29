def divisores_a(n):
    i=1
    suma=0
    while i<n:
        if n%i ==0:
            suma= suma + i
            i+=1
        else:
            i+=1
    return suma  
def numero_perfecto(n):
    if divisores_a(n) == n:
        return True
    else:
        return False
