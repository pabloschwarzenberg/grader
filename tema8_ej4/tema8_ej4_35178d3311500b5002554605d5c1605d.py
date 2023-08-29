from string import ascii_letters
def rot13(palabra):
  abcList = []
  for i in ascii_letters:
    abcList.append(i)
  wordList = []
  for i in palabra:
    wordList.append(i)
  codeList = []
  i = 0
  while i < len(wordList):
    word = wordList[i]
    rotCode = abcList.index(word) + 13
    code = abcList[rotCode]
    codeList.append(code)
    i +=1
  encripted = "".join(codeList).lower()
  return encripted

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           