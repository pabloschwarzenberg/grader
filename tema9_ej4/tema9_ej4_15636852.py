class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self, password):
        l=len(password)

        if 8<=l<=16:
            i=0
            j=0
            k=0

            while i<l:
                try:
                    prueba2=int(password[i])
                    i+=1
                    if i==l:
                        print("La contraseña debe tener al menos un carater en mayuscula")
                        return False
                except ValueError:
                    prueba=password[i].upper()
                    if password[i]==prueba:
                        break
                    i+=1


            while j<l:
                try:
                    prueba=int(password[j])
                    break
                except ValueError:
                    j+=1
                    if j==l:
                        print("La contraseña debe tener numero y caracteres")
                        return False
            while k<l:
                try:
                    prueba=int(password[k])
                    k+=1
                    if k==l:
                        print("La contraseña debe tener numero y caracteres")
                        return False

                except ValueError:
                    break

            self.password=password
            return True

        else:
            print("La contraseña debe tener un mínimo de 8 caracteres y un máximo de 16")
            return False

    def login(self,password):
      if self.password==password:
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