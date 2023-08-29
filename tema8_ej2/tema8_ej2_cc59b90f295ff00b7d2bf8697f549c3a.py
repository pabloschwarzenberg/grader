def buscarTodas(a,b):
    lista = []
    for i in range(len(a)):
        if(a[i]==b):
            lista.append(i)
    if(len(lista)==0):
        return "no existe"
    suma = ""
    for x in lista:
      suma += str(x)
      if lista[-1] == lista[-1]:
        suma += " "
    suma_limpio= str(suma).strip()
    return suma_limpio

if __name__ == "__main__":
  print(buscarTodas("tres tristes tigres","t")) 
