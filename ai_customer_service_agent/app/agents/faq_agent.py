import json

with open("data/faq.json", "r", encoding="utf-8") as f:
    FAQ_DB = json.load(f)

def get_faq_answer(question):
    for item in FAQ_DB:
        if item["question"] in question:
            return item["answer"]
    return "抱歉，这个问题我暂时无法解答，我将为你转人工处理。"
