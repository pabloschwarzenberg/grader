def jerigonzo(string):
    palabra = ""
    for i in string:
      if i in "aeiou":
        palabra = palabra +i+ "p" + i
      else:
        palabra =  palabra + i 
    return palabra

if __name__ == "__main__":
  string = input()
  print(jerigonzo(string))
  pass
         