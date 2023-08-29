class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        self.password=""
        ABC='A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
        abc='a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
        num='0','1','2','3','4','5','6','7','8','9'
        signo_especial='%','/','_'
        contador1=0
        contador2=0
        contador3=0
        contador4=0
        if 8<=len(password)<=16:
                for letra in password:
                    if letra in abc:
                        contador1=contador1+1
                for numero in password:
                     if numero in num:
                        contador2=contador2+1
                for letraMay in password:
                    if letraMay in ABC:
                        contador3=contador3+1
                for especial in password:
                    if especial in signo_especial:
                        contador4=contador4+1
        if contador1>0 and contador2>0 and (contador3>0 or contador4>0):
                return True
        else:
            self.password=""
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