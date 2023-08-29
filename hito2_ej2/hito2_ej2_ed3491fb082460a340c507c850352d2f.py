a = bool
def es_valida(string):
  for i in string:
    if i == "A" or "C" or "T" or "G":
      a = True
    else:
      a = False
    
b = input("Ingrese su codigo de ADN").upper()
es_valida(b)

if a == True:
   print("La secuencia es correcta")
else:
   print("Secuencia incorrecta")