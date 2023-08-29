def hola(a):
    a=a.upper()
    for i in a:
        if (i is not "C") and (i is not "T") and (i is not "G") and (i is not "A"):
          return "secuencia incorrecta"
    return "secuencia correcta"

s=input("")
print(hola(s))