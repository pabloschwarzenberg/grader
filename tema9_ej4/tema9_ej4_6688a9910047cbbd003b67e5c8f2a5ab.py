class Usuario:
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email
        self.password = ""
    def cambiar_password(self,nueva_password):
        if len(nueva_password) >= 8 and len(nueva_password) <= 16:
            abecedario = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
            abecedario_minusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            contador = 0
            for elemento in nueva_password:
                if elemento in abecedario:
                    contador += 1
                if elemento in abecedario_minusculas:
                    contador += 1
            if contador == 0:
                return False

            contador = 0
            numeros = ["0","1","2","3","4","5","6","7","8","9"]
            for elemento in nueva_password:
                if elemento in numeros:
                    contador += 1
            if contador == 0:
                return False

            contador_1 = 0
            for elemento in nueva_password:
                if elemento in abecedario:
                    contador_1 += 1
            abecedario_completo = abecedario + abecedario_minusculas
            letras_y_numeros = abecedario_completo + numeros
            contador_2 = 0
            for elemento in nueva_password:
                if elemento not in letras_y_numeros:
                    contador_2 += 1
            if contador_1 != 0 or contador_2 != 0:
                self.password = nueva_password
                return True
            else:
                return False
        else:
            return False
        
    def login(self,password):
        if password == self.password:
            return True
        else:
            return False
           