def jerigonzo(string):
  #hola   hopolapa
  vocales=['a','á','e','é','i','í','o','ó','u','ú']
  palabranueva=""
  for _ in string:
    if _ in vocales:
      palabranueva= palabranueva+(_)
      palabranueva= palabranueva+('p')
      palabranueva= palabranueva+(_)
    elif _ == ' ':
      palabranueva= palabranueva+(' ')
    else:
      palabranueva= palabranueva+(_)
  
  return palabranueva


if __name__ == "__main__":
  string = input('texto: ')
  string =string.lower()
  print (jerigonzo(string))