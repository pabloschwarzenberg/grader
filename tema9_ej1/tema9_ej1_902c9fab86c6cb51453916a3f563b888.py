from collections import Counter

class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        # Verificar la longitud del tweet
        if len(mensaje) > 140:
            print("El tweet excede el límite de 140 caracteres.")
            return

        # Obtener los hashtags del tweet
        hashtags = [palabra[1:] for palabra in mensaje.split() if palabra.startswith("#")]

        # Actualizar la lista de trending topics
        self.trending_topics.extend(hashtags)

        # Contar la frecuencia de los hashtags
        contador = Counter(self.trending_topics)

        # Obtener los tres hashtags más repetidos
        top_hashtags = contador.most_common(3)

        # Imprimir los resultados
        print("Hashtags más repetidos:")
        for hashtag, frecuencia in top_hashtags:
            print(f"#{hashtag}: {frecuencia} menciones")

# Ejemplo de uso
twitter = Twitter()

# Tweet 1
twitter.tweet("¡Hola mundo! #inicio #saludo")
# Hashtags más repetidos:
# #inicio: 1 menciones
# #saludo: 1 menciones

# Tweet 2
twitter.tweet("Hoy es un día soleado ☀️ #clima #verano")
# Hashtags más repetidos:
# #inicio: 1 menciones
# #saludo: 1 menciones
# #clima: 1 menciones

# Tweet 3
twitter.tweet("¡Feliz viernes a todos! #inicio #saludo #viernes")
# Hashtags más repetidos:
# #inicio: 2 menciones
# #saludo: 2 menciones
# #viernes: 1 menciones

# Tweet 4
twitter.tweet("¡Qué lindo día para pasear! #clima #verano")
# Hashtags más repetidos:
# #inicio: 2 menciones
# #saludo: 2 menciones
# #clima: 2 menciones