from linebot import LineBotApi
from linebot.models import TextSendMessage
import os

# LINEのチャネルアクセストークン（環境変数から取得）
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")

# LINE API クライアントのインスタンスを作成
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

def send_line_reply(reply_token, messages):
    """
    LINEのリプライメッセージを送信する関数
    :param reply_token: LINEのリプライトークン
    :param messages: 送信するメッセージ（リスト形式）
    """
    text_messages = [TextSendMessage(text=msg["text"]) for msg in messages]
    line_bot_api.reply_message(reply_token, text_messages)