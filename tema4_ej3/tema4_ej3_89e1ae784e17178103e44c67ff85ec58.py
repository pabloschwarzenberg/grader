def jerigonzo(string):
  vocales=["a", "e", "i", "o", "u"]
  string_1=list(string)
  s=""
  for i in range(0,len(string_1)):
    s=s+string_1[i]
    if string_1[i] in vocales:
      s=s+"p"+string_1[i]
  return s

if __name__ == "__main__":
  string= input("Ingrese un texto: ")
  print(string_1)
  pass
         