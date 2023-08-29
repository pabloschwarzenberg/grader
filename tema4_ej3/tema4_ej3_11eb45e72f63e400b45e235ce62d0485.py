if __name__ == "__main__":
  def jerigonzo (p):
   p=input("introduzca una palabra: ")
   traductor= ""
   for vocal in p:
     if vocal in "AEIOUaeiou":
      traductor +=vocal
      traductor +="p"
     traductor += vocal
   return print (traductor)