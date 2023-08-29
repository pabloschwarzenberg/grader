def imprimir_string(s):
  # Con for
  for c in s:
    print(c)

def imprimir_string2(s):
  # Ahora con for pero usando indices
  for i in range(len(s)):
    print(s[i])

def imprimir_string3(s):
  count = 0
  while count < len(s):
    print(s[count])
    count += 1

s = input("Ingrese string: ")
imprimir_string(s)
print("###")
imprimir_string2(s)
print("###")
imprimir_string3(s)
print("###")
