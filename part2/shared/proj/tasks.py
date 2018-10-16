from __future__ import absolute_import, unicode_literals
from .celery import app
from .wordcount import WordCount
import json
import os

@app.task
def wordcounter(search_words=False):
    if not search_words:
        search_words = ["han", "hon", "hen", "den", "denne", "denna"] 

    vc = WordCount(search_words)
    
    path = '/home/ubuntu/data/'

    for f in os.listdir(path):
        filename = os.path.join(path, f)
        with open(filename) as file:
            for line in file:
                if (line != '\n'):
                    tweet = json.loads(line)
                    vc.update_counter(tweet['text'])
    return vc.tot_counter

@app.task
def wordcounter_distributed(search_words=False, filename=False):
    if not search_words:
        search_words = ["han", "hon", "hen", "den", "denne", "denna"] 

    vc = WordCount(search_words)
    try: 
        with open(filename) as file:
            for line in file:
                if (line != '\n'):
                        tweet = json.loads(line)
                        vc.update_counter(tweet['text'])
                        
        return vc.tot_counter         
    except:
        print "file is {}".format(filename)
        
              
    
