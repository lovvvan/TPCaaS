from flask import Flask, jsonify
import subprocess
import sys

app = Flask(__name__)

@app.route('/pronoun_counter', methods=['GET'])
def count_pronouns():
    print("Counting pronouns...")
    data = subprocess.check_output(["python3","run_task.py"])
    return data
    
if __name__== '__main__':
    app.run(host='0.0.0.0', debug=True)