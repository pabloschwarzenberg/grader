def jerigonzo(palabra):
    vocales=["a", "e","i","o","u"]
    lista=list(palabra)
    lista_salida=list("")
    i=0
    j=0
    n=0
        
    for n in palabra:
        if lista[i] in vocales:
            lista_salida.append(lista[i])
            lista_salida.append("p")
            lista_salida.append(lista[i])
        else:
            lista_salida.append(lista[i])
        i=i+1
    return "".join(lista_salida)
    #print(lista_salida)
    
if __name__ == "__main__":
  print("bienvenido")
  palabra_a_gerigonciar=input("ingrese palabra agerigonciar:")
  generar_gerigoncio(palabra_a_gerigonciar)
  print(jerigonzo(palabra_a_gerigonciar))        


         