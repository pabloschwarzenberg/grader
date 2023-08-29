class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje) > 140:
            return False
        self.trending_topics.append(i for i in mensaje.split() if i.startswith("#"))