from collections import Counter

class Twitter:
    def __init__(self):
        self.trending_topics = []
    
    def tweet(self, mensaje):
        if len(mensaje) > 140:
            print("Error: El tweet supera los 140 caracteres.")
            return
        
        hashtags = self.extract_hashtags(mensaje)
        self.update_trending_topics(hashtags)
    
    def extract_hashtags(self, mensaje):
        words = mensaje.split()
        hashtags = [word[1:] for word in words if word.startswith("#")]
        return hashtags
    
    def update_trending_topics(self, hashtags):
        self.trending_topics.extend(hashtags)
        
        hashtag_counts = Counter(self.trending_topics)
        top_hashtags = hashtag_counts.most_common(3)
        
        self.trending_topics = [hashtag for hashtag, _ in top_hashtags]
    
    def __repr__(self):
        return str(self.trending_topics)
