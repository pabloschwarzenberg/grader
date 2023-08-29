class Usuario:
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self,password):
        taman = False
        salida = False
        num = False
        mayuscula = False
        letra = False
        especial = False
        
        if len(password) >=8 and len(password)<=16:
            taman = True
        
        for i in password:
            if i.isdigit():
                num = True
                break
        for i in password:
            if i.isupper():
                mayuscula = True
                break       
        for i in password:
            if i.isalpha():
                letra = True
                break
        for i in password:
            if not i.isdigit() and not i.isalpha():
                especial=True
                break
        if (num and letra and taman) and (mayuscula or especial):
            salida = True
            self.password = password
        return salida 

    def login(self,password):
        pas = False
        if password == self.password:
            pas = True
    
        return pas
        

if __name__ == "__main__":
    usuario=Usuario("Aquiles","aqduran@udec.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           