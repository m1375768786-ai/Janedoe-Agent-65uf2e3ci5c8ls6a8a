from app.services.llm_service import call_llm

def classify_intent(user_input):
    prompt = f"""
请对用户问题进行分类：
1. FAQ
2. 技术支持
3. 投诉
4. 订单问题
5. 其他

用户输入：
{user_input}

只输出类别名称：
"""
    return call_llm(prompt)
