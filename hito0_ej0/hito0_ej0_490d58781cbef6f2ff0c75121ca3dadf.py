[11:43, 27/6/2018] Mi Amor: n=int(input())

def cero(n,num=""):
    x=[]
    if len(num)== n:
        return num
    elif len(num)> n:
        return
    else:
        x.append(cero(n,num+"1"))
        x.append(cero(n,num+"0"))
        return x
x=cero(n)
def cambio(lista):
    if type(lista)!=list:
        print(lista)
        return 
    else:
        for i in lista:
            cambio(i)
cambio(x)
[11:43, 27/6/2018] Mi Amor: expresion=input()
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
      x = valores[valores.index("") - 1] * valores[valores.index("") + 1]
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