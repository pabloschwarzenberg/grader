class Usuario:
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self,password):
        tamanio = False
        salida = False
        num = False
        mayuscula = False
        letra = False
        especial = False
        
        if len(password) >=8 and len(password)<=16:
            tamanio = True
        
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
        if (num and letra and tamanio) and (mayuscula or especial):
            salida = True
            self.password = password
        return salida 

    def login(self,password):
        pas = False
        if password == self.password:
            pas = True
    
        return pas
