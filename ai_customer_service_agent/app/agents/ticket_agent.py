from app.database.db import get_conn
from app.agents.routing_agent import route_ticket

def create_ticket(user_input, intent):
    department = route_ticket(intent)

    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tickets (content, category, department, status)
        VALUES (?, ?, ?, ?)
    """, (user_input, intent, department, "OPEN"))

    conn.commit()
    conn.close()

    return f"已为你创建工单，并分配至【{department}】，请耐心等待处理。"
