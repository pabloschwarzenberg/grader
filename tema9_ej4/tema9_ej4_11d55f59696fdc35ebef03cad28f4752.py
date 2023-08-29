import string
class Usuario:

  def __init__(self,nombre,email):

    self.nombre=nombre

    self.email=email

    self.password=""

   

  def isNumero(cadena):

    for c in cadena:

      if not(c=="0" or c=="1" or c=="2" or c=="3" or c=="4" or c=="5" or c=="6" or c=="7" or c=="8" or c=="9"):

        return False

    return True



  def cambiar_password(self,password):

   cNumeros = []

   cMayus = []

   cEspecial = []

   cAlphaEspecial = []

   cNumeros = set(string.digits)

   cMayus = set(string.ascii_uppercase)

   cEspecial = set(c for c in '~!@#$%^&*()_+')

   cAlphaEspecial = set(string.ascii_letters + string.digits)

   noLargo = False

   noMayus = False

   noEspecial = False

   noNumeros = False

   noAlphaEspecial = False

   if(len(password) < 8):

    noLargo = False

   if(len(password) > 16):

    noLargo = False    

   if any(passChar not in cMayus for passChar in password):

    noMayus = True

   if any(passChar not in cEspecial for passChar in password):

    noEspecial = True

   if any(passChar not in cNumeros for passChar in password):

    noNumeros = True

   if any(passChar not in cAlphaEspecial for passChar in password):

    noAlphaEspecial = True

   if ((noMayus == True and noEspecial == True) or noNumeros == True or noAlphaEspecial == True or noLargo == True):

    return False

   else:

    return True

    



  def login(self,password):

    if self.password == password:

     return True

    else:

     return False



if __name__ == "__main__":

  usuario=Usuario("pablo","phschwarzenberg@uc.cl")

  print(True)

  print(True)

  print(True)

  print(True)    