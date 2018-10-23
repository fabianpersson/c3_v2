import re 
from collections import Counter

class WordCount():
    
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.pron_counter = dict.fromkeys(self.dictionary, 0)
        self.tweet_counter = 0
        
    @staticmethod
    def clean(text):
        return re.sub('[^a-zA-Z\s]', "", text.lower())
    
    def count(self, text):
        keywords = filter(lambda x: x in self.dictionary, text.split())
        return Counter(keywords)
    
    def update_counter(self, text):
        text_cleaned = self.clean(text)
        counter = self.count(text_cleaned)
        
        for key in counter.iterkeys():
            self.pron_counter[key] += counter[key]
            
        self.tweet_counter += 1 
        
