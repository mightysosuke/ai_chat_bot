import os
from flask import Flask, request, jsonify
from handlers import handle_message_event

app = Flask(__name__)

@app.route("/callback", methods=["POST"])
def webhook():
    body = request.json
    if body is None:
        return jsonify({"status": "error", "message": "Invalid JSON"}), 400  # エラーハンドリング追加
    events = body.get("events", [])

    for event in events:
        if event.get("type") == "message":
            handle_message_event(event)

    return jsonify({"status": "ok"})

@app.route("/", methods=["GET"])
def index():
    return "LINE Bot is running. Use /webhook for LINE messages.", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))