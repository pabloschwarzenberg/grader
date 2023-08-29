def jerigonzo(string):
  voc=["a","á","e","é","i","í","o","ó","u","ú"]
  palabra=""
  for i in string:
    if i in voc:
      palabra = palabra+(i)
      palabra = palabra+("p")
      palabra = palabra+(i)
    elif i == " ":
      palabra = palabra+(" ")
    else:
      palabra = palabra+(i)
  return palabra

if __name__ == "__main__":
    string=input("Ingrese un texto")
    string = string.lower()
    print(jerigonzo(string))
         