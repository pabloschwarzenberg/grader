class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, clave):
         if len(clave) in list(range(8,17)):
             for i in clave:
                 if i.isalpha():
                     a=[""]
                     for j in clave:
                         if not j.isalpha():
                             a=["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Ñ","Z","X","C","V","B","N","M"]
                             b= ["1","2","3","4","5","6","7","8","9","0"]
                             for w in clave:
                                 if w in a or (not w.isalpha() and w not in b):
                                     self.password=clave
                                     return True
         return False


    def login(self, password):
        return self.password==password