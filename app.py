from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('Xthgy8iO3auvc6rVxKqUllZQypiszZ2NK/Vc3yVp8IuTFlp2L+H7PmUnR4Q9dXNZa988MveIDbOJbW+Ew+jid8Ag1qSQiWykS9UvwHpUfCMKKJPdlKFYrKqwNC8ZKzCDZ8JLiZPZDVwwKfLhjmFS+gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('af56dba71fe5f0b15e1aebf2a7a52cea')


@app.route("/callback", methods=['POST'])  
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if msg in ["hi","Hi"]:
        r = "嗨"
    elif msg == "你吃飯了嗎？":
        r = "還沒，你是誰？"
    elif msg == "你是誰？":
        r = "我是機器人"
    elif "訂位" in msg:
        r = "你想訂位，是嗎？"
        
    r = "I am sorry, I don't know what you said"
    r  = "I don't know what you said"


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text= r))


if __name__ == "__main__":
    app.run()