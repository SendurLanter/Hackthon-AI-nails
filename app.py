from __future__ import unicode_literals
from argparse import ArgumentParser
from flask import Flask, request, abort, jsonify
from linebot import *
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
from flask_cors import CORS
import requests
import sqlite3
import socket
import json
import sys
import os

app = Flask(__name__)
#CORS問題, 每個route位置都要加,沒這行不行
cors = CORS(app, resources={r"/backend": {"origins": "*"}})
channel_secret = '244c0ba6b5b8cfc852215a4d7ec9722f'
channel_access_token ='PnDaadqReQaNS83OOmXr6bhDVNJqHTNQvjcVlPCjLexu7gArCO04YdRlLlwFehrO4HaSfrCDqoKEGwkazzq33lxav6fMGQ8Uca9d2V0HbE6e/FwVcusYq0HgIHCCF9wvKQgOGPFk2+7lXNthp/xunAdB04t89/1O/w1cDnyilFU='
headers = {"Authorization":"Bearer PnDaadqReQaNS83OOmXr6bhDVNJqHTNQvjcVlPCjLexu7gArCO04YdRlLlwFehrO4HaSfrCDqoKEGwkazzq33lxav6fMGQ8Uca9d2V0HbE6e/FwVcusYq0HgIHCCF9wvKQgOGPFk2+7lXNthp/xunAdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}
#line api, 以我line帳號的資訊與line server進行解碼
line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

#主要執行的部分, line server發POST request到callback網址, 在這做解析事件與相對應的動作
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    print(body)
    app.logger.info("Request body: " + body)
    # parse webhook body
    events = parser.parse(body, signature)
    for event in events:
        if event.message.text == "START":
            print('fuck')
            #r = requests.get('http://220.130.195.240:5000/backend')
            HOST, PORT = "140.112.150.95", 11111
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            s.close()
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='OK desu'))

    return 'OK'
#開始執行
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)