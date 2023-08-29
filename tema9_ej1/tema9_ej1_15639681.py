class Twitter:

    def __init__(self):

        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje)<=140:
            k=0
            while k<len(mensaje):

                if mensaje[k]=="#":
                        n=k+1
                        r=""

                        while mensaje[n]!=" ":
                            r+=mensaje[n]
                            n+=1
                            if n==len(mensaje):
                                break

                        if len(self.trending_topics)==0:
                            self.trending_topics.append([r,1])

                        else:
                            l=0

                            while l<len(self.trending_topics):
                                if self.trending_topics[l][0]==r:
                                    self.trending_topics[l][1]=int(self.trending_topics[l][1])+1
                                    break

                                else:
                                    l+=1
                                    if l==len(self.trending_topics):
                                        self.trending_topics.append([r,1])
                                        break

                k+=1

        else:
            pass

if __name__ == "__main__":

    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)