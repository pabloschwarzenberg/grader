def validador(string):
    string=string.upper()
    validador=False
    for i in string:
      if i=="A" or i=="C" or i=="T" or i=="G":
        validador=True
      else:
        validador=False
    if validador == True:
        print("secuencia correcta")
    else:
        print("secuencia incorrecta")



string=str(input())
validador(string)
