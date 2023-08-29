def validarsecuencia(string):
    string=string.upper()
    real=''
    for i in string:
        if i=="A" or i=="C" or i=="T" or i=="G":
            real=real+i
            if len(real)==len(string):
                return 'secuencia correcta'
        else:
            return 'secuencia incorrecta'
      
if __name__ == "__main__":
  s=input("Ingresa un Genoma: ")
  print(validarsecuencia(s))      