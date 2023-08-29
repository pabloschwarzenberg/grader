def jerigonzo(string):
  string = string.replace('a','apa')
  string = string.replace('e','epe')
  string = string.replace('i','ipi')
  string = string.replace('o','opo')
  string = string.replace('u','upu')

  string = string.replace('á','ápá')
  string = string.replace('é','épe')
  string = string.replace('í','ípí')
  string = string.replace('ó','ópó')
  string = string.replace('ú','úpú')

  string = string.replace('A','APA')
  string = string.replace('E','EPE')
  string = string.replace('I','IPI')
  string = string.replace('O','OPO')
  string = string.replace('U','UPU')


  string = string.replace('Á','ÁPÁ')
  string = string.replace('É','ÉPÉ')
  string = string.replace('Í','ÍPÍ')
  string = string.replace('Ó','ÓPÓ')
  string = string.replace('Ú','ÚPÚ')
  return string
  print(string)

if __name__ == "__main__":
    jerigonzo('Eso ya lo sabía')