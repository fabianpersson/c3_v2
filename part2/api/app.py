#!flask/bin/python
from __future__ import absolute_import
from flask import Flask, jsonify
import subprocess
from celery import group
import sys
import os
from proj.tasks import wordcounter_distributed
import time
app = Flask(__name__)


@app.route('/api/v1.0/', methods=['GET'])
def index():
    path = '/home/ubuntu/data/'

    search_words = ["han", "hon", "hen", "den", "denne", "denna"] 
    tot_counter = dict.fromkeys(search_words, 0)
    task_list = []
    
    file_list = [os.path.join(path, f ) for f in os.listdir(path)]

    jobs = group(wordcounter_distributed.s(search_words, filename) for filename in file_list)
    result = jobs()
    res = result.get()
    
    
    #group()
    #for f in os.listdir(path):
    #    filename = os.path.join(path, f)
        
        
 
    #    res = wordcounter_distributed.delay(search_words, filename)
    #    task_list.append(res)
        
    #time_start = time.time()
    #counter = 0
    
    #for res in task_list: #for each task
    
    #    try:
     #       response = res.get()
      #      for search_word in response.iterkeys(): #for each key
       #         tot_counter[search_word] += response[search_word]
        #    counter+=1
         #   print "complete task {} out of {} in {}".format(counter, len(task_list),time.time()-time_start)
        #except Exception as e:
         #   print "error: {}".format(e)
          #  print "at task with id {}".format(res.id)
    return jsonify(res)

if __name__ == '__main__':
    
    app.run(host='0.0.0.0',debug=True)

