#!/usr/bin/env python
# coding: utf-8

# In[5]:


from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os

# アクセストークンとシークレット（直書き or 環境変数）
CHANNEL_ACCESS_TOKEN = ("f+Q1kdvvcQ4WZNyGqrZAy/cn5fGPpFn0OYaxsq8vPWEmoRbmCyAgwFXjZZ6TrDO0vOeOD1On9OrldXXTF+O0AqZu9aat5mvHb3lG7DDR6GB5TaKU/eZWRgszUdVnCIgQt8fe/DhG1Fsp+QdiW/PRJAdB04t89/1O/w1cDnyilFU=")
CHANNEL_SECRET = ("06a8520ebc8b3efbcf84386f41800ca8")

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

app = Flask(__name__)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text

    if user_message == "こんにちは":
        reply = "こんにちは！映画の記録ならlineboyにお任せ！"
    else:
        reply = "『映画登録 タイトル:〇〇』って送ってみてね！"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply)
    )

if __name__ == "__main__":
    app.run(port=5000)

