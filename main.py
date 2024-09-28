from flask import Flask
import os
from redis import Redis

app = Flask(__name__)
redis = Redis(host=os.environ.get('REDIS_HOST', 'localhost'), port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return f'Hello! This page has been viewed {count} times.\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)