def jerigonzo (p):
  traductor= ""
  for vocal in p:
    if vocal in "AEIOUaeiou":
     traductor +=vocal
     traductor +="p"
    traductor += vocal
  return print (traductor)
a=jerigonzo(input("Introduzca una palabra para traducirla en jerigonzo: "))
print (a)