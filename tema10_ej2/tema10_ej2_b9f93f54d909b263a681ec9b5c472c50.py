#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    pass

if __name__=="__main__":
    pass
    
  levenshtein <- function(str_1, str_2) {
  distance   <- levenshtein_distance(str_1, str_2)
  similarity <- 1 - distance / max(str_length(str_1), str_length(str_2))
  return(similarity)
}