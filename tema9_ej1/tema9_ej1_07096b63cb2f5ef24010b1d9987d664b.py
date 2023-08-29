class Twitter: # Auto es el nombre de la clase

    # esto __init__ es el contructor, permite inicializar los atributos
    def __init__(self): # self es un parametro con el que nos permite trabajar con la clase,es una especie de referencia hacia el mismo objeto
        self.trending_topics = []

    def tweet(self,mensaje):
        self.tweet = mensaje


a = Twitter()
a.tweet("gano #laroja")


if a.tweet == "gano #laroja":
    twitter=Twitter()
    twitter.trending_topics

elif a.tweet == "grande #chile":
    twitter=Twitter()
    twitter.trending_topics

elif a.tweet == "#laroja con dos goles, le gano a brasil, grande #laroja":
    twitter=Twitter()
    twitter.trending_topics
    twitter.trending_topics


