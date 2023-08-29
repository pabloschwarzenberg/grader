class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        largo=len(password)
        digitos=["0","1","2","3","4","5","6","7","8","9"]
        letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        lista=[]
        for i in range(len(password)):
            if password[i] in digitos:
                lista.append("Numero")
            if password[i] in letras:
                lista.append("Letra")
            for j in range(len(letras)):
                if password[i] == letras[j].upper():
                    lista.append("Mayuscula")
            if len(lista)<(i+1):
                lista.append("C.Esp.")
        if ((largo>=8) and (largo<=16) and ("Numero" in lista) and ("Letra" in lista) and (("Mayuscula" in lista) or ("C.Esp." in lista))):
            self.password=password
            return True
        else:
            return False

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
           