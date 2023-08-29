def substrings_unicos(s, n):
  substrings = []
  ocurrencias = {}

  for i in range(len(s) - n + 1):
    substring = s[i:i+n]

    if substring in ocurrencias:
      ocurrencias[substring] += 1
    else:
      ocurrencias[substring] = 1
  
  for substring, valor in ocurrencias.items():
    if valor == 1:
      substrings.append(substring)
  
  return substrings

s = input("Ingrese un string: ")
n = int(input("Ingrese un entero n: "))
resultado = substrings_unicos(s, n)

if len(resultado) == 0:
  print("ninguna")
else:
  for substring in resultado:
    print(substring)      