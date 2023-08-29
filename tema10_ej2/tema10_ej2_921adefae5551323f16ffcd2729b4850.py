#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
levenshtein_distance <- function(str_1, str_2) {
  str_1 <- tolower(str_1)
  str_2 <- tolower(str_2)
  if (str_length(str_1) == 0 || str_length(str_2) == 0) {
    return(max(str_length(str_1), str_length(str_2)))
  }
  previous_row <- 0:str_length(str_2);
  for (i in 1:str_length(str_1)) {
    current_row    <- rep(0, str_length(str_2))
    current_row[1] <- i
    for (j in 1:str_length(str_2)) {
      insertions         <- previous_row[j + 1] + 1
      deletions          <- current_row[j] + 1
      substitutions      <- previous_row[j] + (str_sub(str_1, i, i) != str_sub(str_2, j, j))
      current_row[j + 1] <- min(insertions, deletions, substitutions)
    }
    previous_row <- current_row
  }
  return(current_row[length(current_row)])
}