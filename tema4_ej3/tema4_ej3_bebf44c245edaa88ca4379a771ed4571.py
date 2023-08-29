def jerigonzo(string):
  secuencia=list(string)
  vocales=["a","e","i","o","u"]
  i=0
  string=string.replace("a","apa")
  string=string.replace("e","epe")
  string=string.replace("i","ipi")
  string=string.replace("o","opo")
  string=string.replace("u","upu")
  
  return string


if __name__ == "__main__":
    string=input("")
    print(jerigonzo(string))
         