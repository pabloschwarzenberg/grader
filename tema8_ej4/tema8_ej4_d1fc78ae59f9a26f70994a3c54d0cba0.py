def rot13(palabra):
    abecedario="abcdefghijklmnopqrstuvwxyz"
    lista_abc= list(abecedario)
    lista_palabra= list(palabra)
    resultado=[]
    i=0
    for letra in lista_palabra:
       posicion= lista_abc.index(letra)
       nueva_posicion= posicion+13
       if nueva_posicion>25:
          nueva_n_posicion= nueva_posicion-26
          letra_codificada= lista_abc[nueva_n_posicion]
          resultado.append(letra_codificada)
       else:
          letra_codificada= lista_abc[nueva_posicion]
          resultado.append(letra_codificada)
       
    resultado_final= "".join(resultado)
    return resultado_final
       
       

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           