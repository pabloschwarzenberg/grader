def secuencia(string):
  DNA=list(string)
  for i in DNA:
    if i!="A" and i!="C" and i!="T" and i!="G" and i!="a" and i!="c" and i!="t" and i!="g":
        return "secuencia incorrecta"
  return "secuencia correcta"

string=input("Ingrese una secuencia: ")
print(secuencia(string))