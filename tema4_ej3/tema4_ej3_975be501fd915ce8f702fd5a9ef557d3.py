def jerigonzo(string):
  stringTraducida = ""
  vocales=['a','A','e','E','i','I','o','O','u','U']
  for i in string:
    stringTraducida = stringTraducida + i
    if i in vocales:
      stringTraducida = stringTraducida + "p" + i
  return stringTraducida
if __name__ == "__main__":
    string=input("Ingrese palabra: ")
    programa=jerigonzo(string)
    print(programa)