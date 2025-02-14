from line_utils import send_line_reply
from gemini_utils import get_gemini_response

# ユーザーごとのチャット状態を管理する辞書
user_sessions = {}

def handle_message_event(event):
    user_id = event["source"]["userId"]
    user_message = event["message"]["text"]
    reply_token = event["replyToken"]
    print(event)

    # 「チャット開始」と送られた場合、キャラクター選択を促す
    if user_message == "チャット開始":
        user_sessions[user_id] = None  # キャラクター未選択状態にリセット
        message = {
            "type": "text",
            "text": "キャラクターや有名人の名前を書いてください"
        }
        print(message)
        send_line_reply(reply_token, [message])
        return

    # ユーザーがキャラクター未選択の場合（最初の入力をキャラクター名と見なす）
    if user_id not in user_sessions or user_sessions[user_id] is None:
        user_sessions[user_id] = user_message  # 入力をキャラクターとして保存
        message = {
            "type": "text",
            "text": f"{user_message} を選択しました！チャットを開始してください。"
        }
        send_line_reply(reply_token, [message])
        return

    # 「終了」と送られた場合、チャットを終了する
    if user_message == "終了":
        user_sessions.pop(user_id, None)  # セッションを削除
        message = {
            "type": "text",
            "text": "チャットを終了しました。また話したくなったら「チャット開始」と送ってください。"
        }
        send_line_reply(reply_token, [message])
        return

    # 既にキャラクターを選択している場合、Gemini API で応答を生成
    selected_character = user_sessions[user_id]
    gemini_response = get_gemini_response(selected_character, user_message)

    # Geminiの応答を送信
    message = {
        "type": "text",
        "text": gemini_response
    }
    send_line_reply(reply_token, [message])
