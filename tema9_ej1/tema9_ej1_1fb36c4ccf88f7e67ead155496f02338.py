"""
Ejercicio Twitter Hito3
"""


class Twitter:
    def __init__(self):
        self.trending_topics = {}


    def tweet(self, mensaje):
        if len(mensaje) <= 140:

            tweeto = mensaje.strip(",.").split()

            for trend in tweeto:
                if trend[0] == "#":
                    if trend not in self.trending_topics:
                        self.trending_topics[trend] = 1
                    else:
                        self.trending_topics[trend] += 1




            d_inv = {v: k for k, v in self.trending_topics.items()}
            values = list(self.trending_topics.values())
            try:
                values.sort()
                values = values[-3::]
                values.reverse()
                for k in values:
                    print("Los hashtags más usados son: \n")
                    print(d_inv[k])
            except IndexError:
                for item in self.trending_topics:
                    print(item)
            # def __repr__(self):
            #     out = []
            #     for item in self.trending_topics:
            #         c = self.trending_topics.count(item)
            #         if [item, c] not in out:
            #             out.append.([item, c])
            #     return(str(out))
            return True
        else:
            print("Debes ingresar un texto de maximo 140 caraceteres")
            return False
if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    twitter.tweet("#gonano es el rey de la #tierra, me importa un #pico #laroja")
    print(twitter.trending_topics)
           