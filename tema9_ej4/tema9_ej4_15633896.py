class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):

        if len(password) > 16 or len(password)<8 :
            print("La contraseña debe tener entre 8 y 16 caracteres")
            return False

        numeros="123456789"
        letras="abcdefghijklmnñopqrstuvwxyz"
        mayusculas=letras.upper()

        lista=list(password)
        lista.sort()

        print(lista)

        lnumeros=[]
        lminusculas=[]
        lmayusculas=[]
        lsimbolos=[]

        for i in lista:
            if numeros.find(i)!=-1:
                lnumeros.append(i)
  
        for i in lista:
            if letras.find(i)!=-1:
                lminusculas.append(i)

        for i in lista:
            if mayusculas.find(i)!=-1:
                lmayusculas.append(i)

        for i in lista:
            if numeros.find(i)==-1 and letras.find(i)==-1 and mayusculas.find(i)==-1:
                lsimbolos.append(i)

        print(lnumeros)
        print(lminusculas)
        print(lmayusculas)
        print(lsimbolos)

        if len(lnumeros)==0:
            print("Tu contraseña debe incluir al menos un numero")
            return False

        elif len(lminusculas)==0:
            print("Tu contraseña debe tener al menos una letra minuscula")
            return False

        elif len(lmayusculas)==0 and len(lsimbolos)==0:
            print("La constraseña debe tener al menos una letra mayuscula o un simbolo")
            return False
        else:

            self.password=password
            return True

 
    def login(self,password):

        if password==self.password:
            return True
        else:
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
           