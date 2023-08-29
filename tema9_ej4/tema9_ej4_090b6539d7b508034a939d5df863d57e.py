class Usuario:
  def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""
  def cambiar_password(self,password):
    def analisis_palabra(password):
      alfespanol = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ñ', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                    't', 'u', 'v', 'w', 'x', 'y', 'z']
      nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
      aprobada = False
      if 16 >= len(password) >= 8:
        minusculas = 0
        mayusculas = 0
        numeros = 0
        especiales = 0
        for caracter in password:
          mi = False
          ma = False
          nu = False
          es = False
          for letra in alfespanol:
            if caracter == letra:
              mi = True
            if caracter == letra.upper():
              ma = True
          for num in nums:
            if caracter == num:
              nu = True
          if not mi and not ma and not nu:
            es = True
          if mi:
            minusculas += 1
          if ma:
            mayusculas += 1
          if nu:
            numeros += 1
          if es:
            especiales += 1
        if numeros > 0 and minusculas > 0 and (mayusculas > 0 or especiales > 0):
          aprobada = True
      return (aprobada)
    f = False
    if analisis_palabra(password):
      self.password = password
      f = True
    return(f)
  def login(self,password):
    if password == self.password:
      return(True)
    else:
      return(False)    