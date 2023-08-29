def buscarTodas(a,b):
    str_to_list = list(a)
    resultado = ""
    for i in range(0, len(str_to_list)):
      if str_to_list[i] == b:
        resultado = resultado + str(i) + " "
    resultado = resultado.strip()
    return resultado

if __name__ == "__main__":
    pass
    

           