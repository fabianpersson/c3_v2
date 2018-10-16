#!flask/bin/python
from __future__ import absolute_import
from flask import Flask, jsonify
import subprocess
import sys
import os
from proj.tasks import wordcounter_distributed
app = Flask(__name__)


@app.route('/api/v1.0/', methods=['GET'])
def index():
    path = '/home/ubuntu/data/'

    search_words = ["han", "hon", "hen", "den", "denne", "denna"] 
    tot_counter = dict.fromkeys(search_words, 0)
    task_list = []

    for f in os.listdir(path):
        filename = os.path.join(path, f)
        
        res = wordcounter_distributed.delay(search_words, filename)
        task_list.append(res)
     
    for res in task_list: #for each task
        try:
            response = res.get()
            for search_word in response.iterkeys(): #for each key
                tot_counter[search_word] += response[search_word]

            print("counter is", response)
        except:
            print "could not process task with id {}".format(res.id)
    return jsonify(tot_counter)

if __name__ == '__main__':
    
    app.run(host='0.0.0.0',debug=True)

