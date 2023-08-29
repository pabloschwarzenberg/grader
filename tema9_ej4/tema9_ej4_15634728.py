class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if not 8 <= len(password) <= 16:
            return False
        minus = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        mayus = [letra.upper() for letra in minus]
        numer = [str(i) for i in range(10)]
        n_min,n_may,n_num,n_otr = 0,0,0,0
        for letra in password:
            if letra in minus:
                n_min += 1
            elif letra in mayus:
                n_may += 1
            elif letra in numer:
                n_num += 1
            else:
                n_otr += 1
        if n_min == 0 and n_may == 0:
            return False
        if n_num == 0:
            return False
        if n_may == 0 and n_otr == 0:
            return False
        self.password = password
        return True
                
    def login(self,password):
        if self.password == password:
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