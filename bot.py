from flask import Flask, request
import config
import os
import random

server = Flask(__name__)


print("in bot.py")

@server.route("/")
def webhook():
    
    return "ok", 200
#dvach
@server.route("/wakeup")
def wakeup():
    #print("pinged")
    return "Never sleeps", 200


import NotSleeping
print("in bot.py(1)")
server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
server = Flask(__name__)
