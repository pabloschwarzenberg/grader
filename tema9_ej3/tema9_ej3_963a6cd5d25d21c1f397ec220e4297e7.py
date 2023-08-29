def decodificar(mensaje):
    numeros_binarios = mensaje.split(',')
    letras = [chr(int(numero_binario, 2)) for numero_binario in numeros_binarios]
    mensaje_descifrado = ''.join(letras)
    return mensaje_descifrado

#MULTIPLICACION DE MATRICES
class Matriz:
    def __init__(self, celdas=[]):
        self.celdas = celdas

    def __repr__(self):
        s = ""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s += "{0: >5} ".format(self.celdas[i][j])
            s += "\n"
        return s

    def __mul__(self, other):
        if len(self.celdas[0]) != len(other.celdas):
            raise ValueError("Las dimensiones de las matrices no son compatibles para la multiplicaciÃ³n.")

        result = Matriz([[0] * len(other.celdas[0]) for _ in range(len(self.celdas))])

        for i in range(len(self.celdas)):
            for j in range(len(other.celdas[0])):
                for k in range(len(other.celdas)):
                    result.celdas[i][j] += self.celdas[i][k] * other.celdas[k][j]

        return result

if __name__ == "main":
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r = a * b
    print(r)
    
#TWITTER
class Twitter:
    def __init__(self):
        self.trending_topics = []
    def tweet(self, message):
        if len(message) > 140:
            print("El tweet excede la longitud mÃ¡xima de 140 caracteres.")
            return
        hashtags = [word[1:] for word in message.split() if word.startswith("#")]
        for hashtag in hashtags:
            self.update_trending_topics(hashtag)
    def update_trending_topics(self, hashtag):
        for topic in self.trending_topics:
            if topic[0] == hashtag:
                topic[1] += 1
                return
        self.trending_topics.append([hashtag, 1])
    def get_top_trending_topics(self):
        sorted_topics = sorted(self.trending_topics, key=lambda x: x[1], reverse=True)
        top_topics = sorted_topics[:3]
        return top_topics