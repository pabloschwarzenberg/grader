special = "!@#$%^&*()-+?_=,<>/"
class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        char = False
        let = False
        if len(password) >= 8 and len(password) <=16 :
          for letra in password :
            if letra.isupper() or letra in special:
              char = True
            elif letra.isnumeric():
              let = True
          if char and let:
            self.password = str(password)
            return True
        return False
    def login(self,password):
        if password == self.password:
          return True
        return False
        
if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))

#Decodificador
def decodificar(mensaje):
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
  
def decodificar(mensaje):
    a = str(mensaje[0:8])
    decimal_1 = (int(str(a), 2))
    letra_1 = chr(decimal_1)
    b = str(mensaje[10:17])
    decimal_2 = (int(str(b), 2))
    letra_2 = chr(decimal_2)
    c = str(mensaje[19:26])
    decimal_3 = (int(str(c), 2))
    letra_3 = chr(decimal_3)
    d = str(mensaje[28:35])
    decimal_4 = (int(str(d), 2))
    letra_4 = chr(decimal_4)
    palabra = letra_1 + letra_2 + letra_3 + letra_4
    return palabra
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)

#Multiplicación de matrices
class Matriz:
    def __init__(self,celdas=[]):
        self.celdas=celdas

    def __repr__(self):
        s=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
        return s

    def __mul__(self, other):
          m = Matriz([])
          m=Matriz([[self.celdas[0][0]*other.celdas[0][0]+self.celdas[0][1]*other.celdas[1][0],
             self.celdas[0][0]*other.celdas[0][1]+self.celdas[0][1]*other.celdas[1][1]],
             [self.celdas[1][0]*other.celdas[0][0]+self.celdas[1][1]*other.celdas[1][0],
             self.celdas[1][0]*other.celdas[0][1]+self.celdas[1][1]*other.celdas[1][1]]])
          return m

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)           