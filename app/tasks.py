from celery import Celery
import json
import os

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')

@app.task
def pronoun_count(folder):
    pronoun_list = ['han', 'hon', 'den', 'det', 'denna', 'denne', 'hen']
    pronoun_count = dict.fromkeys(pronoun_list, 0)
    list_of_files = os.listdir(folder)
    for one_file in list_of_files:
        f = open(folder + one_file)
        lines = f.readlines()
        for line in lines:
            if line.strip():
                dic = json.loads(line)
                if "retweeted_status" not in dic:
                    list_of_words = dic['text'].split(" ")
                    for word in list_of_words:
                        word = word.strip(' .,:;!?')
                        word = word.lower()
                        if word in pronoun_list:
                            pronoun_count[word] += 1
    return pronoun_count