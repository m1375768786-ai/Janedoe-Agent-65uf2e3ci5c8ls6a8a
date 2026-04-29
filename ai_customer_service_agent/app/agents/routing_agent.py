def route_ticket(intent):
    mapping = {
        "技术支持": "技术部",
        "投诉": "客服主管",
        "订单问题": "订单中心",
        "其他": "人工客服"
    }
    return mapping.get(intent.strip(), "人工客服")
