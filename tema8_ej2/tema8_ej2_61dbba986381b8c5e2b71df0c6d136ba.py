def buscarTodas(Oracion, Letra):
    Follow = -1
    Str_Vacio = ""
    Split = " "
    for a in Oracion:
        Follow += 1
        if Letra in a:
            Str_Vacio += str(Follow)
            Str_Vacio += Split
    return Str_Vacio[:-1]
if __name__ == "__main__":
  Oracion_1 = str(input("Ingrese una oración: "))
  Letra_1 = str(input("Ingrese una letra: "))
  Final = buscarTodas(Oracion_1, Letra_1)
  print(Final)