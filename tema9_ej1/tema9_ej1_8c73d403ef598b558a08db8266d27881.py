class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, message):
        # Verificar si el tweet supera el límite de 140 caracteres
        if len(message) > 140:
            print("El tweet excede el límite de 140 caracteres")
            return

        # Buscar hashtags en el mensaje y actualizar su contador en la lista de trending topics
        hashtags = self.extract_hashtags(message)
        for hashtag in hashtags:
            self.update_trending_topics(hashtag)

        # Mostrar los tres hashtags más repetidos
        self.show_top_trending_topics()

    def extract_hashtags(self, message):
        words = message.split()
        hashtags = [word.strip("#") for word in words if word.startswith("#")]
        return hashtags

    def update_trending_topics(self, hashtag):
        # Buscar el hashtag en la lista de trending topics
        for topic in self.trending_topics:
            if topic["hashtag"] == hashtag:
                topic["count"] += 1
                return

        # Si el hashtag no existe, agregarlo a la lista de trending topics
        self.trending_topics.append({"hashtag": hashtag, "count": 1})

    def show_top_trending_topics(self):
        # Ordenar los trending topics por su contador de forma descendente
        sorted_topics = sorted(self.trending_topics, key=lambda x: x["count"], reverse=True)

        # Mostrar los tres hashtags más repetidos
        print("Trending Topics:")
        for i, topic in enumerate(sorted_topics[:3]):
            print(f"{i+1}. #{topic['hashtag']} - {topic['count']} menciones")


# Ejemplo de uso
if __name__ == "__main__":
    twitter = Twitter()

    twitter.tweet("Este es un tweet de ejemplo #python #programacion")
    twitter.tweet("¡Hoy es un buen día para programar en #python!")
    twitter.tweet("Me encanta utilizar hashtags en mis tweets #hashtags #twitter")
    twitter.tweet("Estoy aprendiendo #python y #programacion")
    twitter.tweet("#programacion es divertida y desafiante")

