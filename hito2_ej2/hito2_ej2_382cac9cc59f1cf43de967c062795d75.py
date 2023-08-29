def validar(s):
  s=s.lower()
  for letra in s:
    if letra not in "actg":
      return "secuencia correcta"
    else:
      return "secuencia incorrecta"

a=input()
print(validar(a))
     