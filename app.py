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
    s = "Have you a dinner?"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text= s))


if __name__ == "__main__":
    app.run()