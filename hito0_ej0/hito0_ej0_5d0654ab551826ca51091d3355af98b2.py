#El codigo es de Sebastian Lepe, Joaquin Hernandez, Marco Troncoso, Baltasar Luco, Sebastian Vilaza
expresion=input()
expresion=list(expresion)
x=[]
lista = []
for i in range(len(expresion)):
    if expresion[i].isnumeric()==True:
        lista.append(expresion[i])
    else:
        lista="".join(lista)
        if len(lista)!=0:
            x.append((float(lista)))
            x.append(expresion[i])
            lista=[]
lista = "".join(lista)
x.append((float(lista)))
def interpretar(valores):
  if len(valores)==1:
      return valores[0]

  elif "/" in valores:
      x=valores[valores.index("/")-1]/valores[valores.index("/")+1]
      valores.insert(valores.index("/")-1,x)
      valores.pop(valores.index("/")-1)
      valores.pop(valores.index("/")+1)
      valores.pop(valores.index("/"))
      return interpretar(valores)
  elif "*" in valores:
      x = valores[valores.index("*") - 1] * valores[valores.index("*") + 1]
      valores.insert(valores.index("*") - 1, x)
      valores.pop(valores.index("*") - 1)
      valores.pop(valores.index("*") + 1)
      valores.pop(valores.index("*"))
      return interpretar(valores)
  elif "-" in valores:
      x = valores[valores.index("-") - 1] - valores[valores.index("-") + 1]
      valores.insert(valores.index("-") - 1, x)
      valores.pop(valores.index("-") - 1)
      valores.pop(valores.index("-") + 1)
      valores.pop(valores.index("-"))
      return interpretar(valores)
  elif "+" in valores:
      x = valores[valores.index("+") - 1] + valores[valores.index("+") + 1]
      valores.insert(valores.index("+") - 1, x)
      valores.pop(valores.index("+") - 1)
      valores.pop(valores.index("+") + 1)
      valores.pop(valores.index("+"))
      return interpretar(valores)

print(interpretar(x))
#el resultado debiera ser 15.66666
      