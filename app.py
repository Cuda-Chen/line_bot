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

line_bot_api = LineBotApi('VMXzbphrpR9UVV7WmuPylRmiyNXXaxiNAeyso+UloPDPcnyphBWdz4mYRkaZj6YK2QJrwYIKVcQ64XRhazX8Ve2DMoVnUYzBcYKt/bECupDe6MkK8dg5QAiJl9ms2ohTOWoK7Bf/c8XoqKAsbXY+WQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('1ceef6519472f8aba6671d9413151c7b')

@app.route("/callback", methods=['POST'])
def callback():
	signature = request.headers['X-Line-Signature']
	body = request.get_data(as_text=True)
	app.logger.info("Request body: " + body)
	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		abort(400)
	return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	#line_bot_api.reply_message(
	#	event.reply_token,
	#	TextSendMessage(text=event.message.text))
	message = TextSendMessage(text='Hello World')
	line_bot_api.reply_message(event.reply_token, message)
if __name__ == "__main__":
	app.run()
