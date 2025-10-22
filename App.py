# app.py
from flask import Flask, render_template_string, request, redirect, url_for
import redis
import os

app = Flask(__name__)
# Connect to Redis. The hostname will be passed as an environment variable.
redis_host = os.environ.get('REDIS_HOST', 'localhost')
r = redis.Redis(host=redis_host, port=6379, db=0, decode_responses=True)

@app.route('/')
def index():
    votes_cat = r.get('cat') or 0
    votes_dog = r.get('dog') or 0

    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Cat vs Dog</title>
            <style>
                body { font-family: sans-serif; text-align: center; }
                .container { display: flex; justify-content: center; gap: 40px; }
                button { font-size: 1.2em; padding: 10px 20px; }
                .results { margin-top: 40px; font-size: 1.5em; }
            </style>
        </head>
        <body>
            <h1>Which do you prefer?</h1>
            <div class="container">
                <div><h2>Cats</h2><form action="/vote" method="post"><button name="vote" value="cat">Vote Cat</button></form></div>
                <div><h2>Dogs</h2><form action="/vote" method="post"><button name="vote" value="dog">Vote Dog</button></form></div>
            </div>
            <div class="results"><strong>Cat Votes:</strong> {{ votes_cat }} | <strong>Dog Votes:</strong> {{ votes_dog }}</div>
        </body>
        </html>
    ''', votes_cat=votes_cat, votes_dog=votes_dog)

@app.route('/vote', methods=['POST'])
def vote():
    choice = request.form['vote']
    if choice == 'cat':
        r.incr('cat')
    elif choice == 'dog':
        r.incr('dog')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
