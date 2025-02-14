import requests

LINE_CHANNEL_ACCESS_TOKEN = "J6vmTwBpFA6ewJYyPidOZqkRcorg9prRxq9+JUp3fhLV6XBkqDqvs98zO1XGZSZyI7FaduJQRbS1s6RwyQYhJLLRCohcZZMI8Tm7PkccGEJbuXR5u1AeQLPp0pdYo6BZA6M9bv9HciEacXMX2M6WNwdB04t89/1O/w1cDnyilFU="

# Helper function to send a reply via LINE Messaging API
def send_line_reply(reply_token, messages):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LINE_CHANNEL_ACCESS_TOKEN}"
    }
    payload = {
        "replyToken": reply_token,
        "messages": messages
    }
    response = requests.post("https://api.line.me/v2/bot/message/reply", headers=headers, json=payload)
    return response.status_code
