import os
import google.generativeai as genai

# Gemini APIの設定
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

def get_gemini_response(character, user_message):
    """ 指定キャラクターになりきってGemini APIで応答を生成 """
    prompt = f"あなたは{character}です。以下のメッセージにキャラクターになりきって返信してください。\n\nユーザー: {user_message}"

    try:
        response = model.generate_content(prompt)
        return response.text if response else "申し訳ありませんが、少し時間をおいて再試行してください。"
    except Exception as e:
        return f"エラーが発生しました: {str(e)}"
