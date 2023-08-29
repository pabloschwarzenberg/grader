def jerigonzo(string):
  string = string.replace('a','apa')
  string = string.replace('e','epe')
  string = string.replace('i','ipi')
  string = string.replace('o','opo')
  string = string.replace('u','upu')

  string = string.replace('á','apa')
  string = string.replace('é','epe')
  string = string.replace('í','ipi')
  string = string.replace('ó','opo')
  string = string.replace('ú','upu')

  string = string.replace('A','apa')
  string = string.replace('E','epe')
  string = string.replace('I','ipi')
  string = string.replace('O','opo')
  string = string.replace('U','upu')


  string = string.replace('Á','apa')
  string = string.replace('É','epe')
  string = string.replace('Í','ipi')
  string = string.replace('Ó','opo')
  string = string.replace('Ú','upu')
  return string
  print(string)

if __name__ == "__main__":
    jerigonzo('Eso ya lo sabía')
