 
def validar_secuencia(string):
   string = string.lower()
   for caracter in string:
       if caracter not in "actg":
         return False
   return True
 
string=input("")
respuesta = validar_secuencia(string)
if respuesta:
  print("secuencia correcta")
else:
  print ("secuencia incorrecta")