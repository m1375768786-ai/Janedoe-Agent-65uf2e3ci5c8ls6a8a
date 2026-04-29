from app.agents.intent_agent import classify_intent
from app.agents.decision_agent import should_auto_resolve
from app.agents.faq_agent import get_faq_answer
from app.agents.ticket_agent import create_ticket
from app.database.db import init_db

def handle_request(user_input):
    print("🔍 正在分析用户意图...")
    intent = classify_intent(user_input)
    print(f"📌 识别意图: {intent}")

    if should_auto_resolve(intent):
        print("🤖 自动处理...")
        return get_faq_answer(user_input)
    else:
        print("📄 创建工单...")
        return create_ticket(user_input, intent)

if __name__ == "__main__":
    init_db()

    print("===== AI客服系统启动 =====")
    while True:
        user_input = input("\n用户: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        response = handle_request(user_input)
        print("AI:", response)
