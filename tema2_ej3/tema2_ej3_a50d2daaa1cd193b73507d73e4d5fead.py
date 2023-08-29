#Numeros perfectos
# el cálculo en sí lo tube que buscar y copiar,
# sabia que era algo parecido a lo de los primos pero
# no supe hacerlo a excepción de la estructura en sí.
def numero_perfecto(a):
    suma=0
    for B in range(1,a//2+1):
        if(a%B==0):
            suma+=B
    if(suma==a):
        return True
    else:
        return False

if __name__=="__main__":
  pass