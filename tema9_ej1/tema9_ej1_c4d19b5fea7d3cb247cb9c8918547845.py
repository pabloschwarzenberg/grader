class Twitter:

    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):

        hashtags = []
        hashtag=[]
        hashtagf = []

        if len(mensaje)<=140:

            k = 0
            for i in range(len(mensaje)):

                if mensaje[i] == '#':


                    for t in range(i,len(mensaje)):

                        if mensaje[t] != ' ':

                            hashtag.append(mensaje[t])

                        else:
                            break

                    hashtag = ''.join(hashtag)
                    hashtags.append(hashtag)
                    hashtag = []
                        #DEBUG THIS




            if hashtags != []:

                if len(hashtags)<=3:

                    self.trending_topics = hashtags

                else:

                    for x in range(len(hashtags)):

                        if hashtags.count(hashtags[x])>1:

                            if hashtags[x] not in hashtagf:

                                hashtagf.append(hashtags[x])


        else:

            self.trending_topics = []

        return self.trending_topics
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           