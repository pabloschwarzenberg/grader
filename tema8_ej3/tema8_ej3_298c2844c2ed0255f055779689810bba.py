#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales

estadisticas_frase=lambda x: tuple((len(x.split()),len(x),len(x.strip('.').replace(' ','').replace('\n',''))/len(x.split()),x.count(' '),x.count('.')))

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         