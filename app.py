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

# Channel Access Token
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

	# send help message
	if event.message.text == u'!9':
		line_bot_api.reply_message(event.reply_message, 'help')
	elif event.message.text == u'最近避難所':
		line_bot_api.reply_message(event.reply_message, 'shelter')
	elif event.message.text == u'物資':
		line_bot_api.reply_message(event.reply_message, 'resource')
	elif event.message.text == u'避難準備':
		line_bot_api.reply_message(event.reply_message, 'preparation')
	elif event.message.text == u'其他':
		line_bot_api.reply_message(event.reply_message, 'others')
	else:
		message = TextSendMessage(text='Hello World')
		line_bot_api.reply_message(event.reply_token, message)
if __name__ == "__main__":
	app.run()
