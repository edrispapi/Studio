# studio_agent.py

def input_node(data):
    # اعتبارسنجی داده ورودی
    required_keys = {"today", "yesterday"}
    for key in required_keys:
        if key not in data:
            raise ValueError(f"Missing key: {key}")
    for day in ["today", "yesterday"]:
        for field in ["revenue", "cost", "number_of_customers"]:
            if field not in data[day]:
                raise ValueError(f"Missing field: {field} in {day}")
    return data

def processing_node(data):
    today = data['today']
    yesterday = data['yesterday']
    profit = today['revenue'] - today['cost']
    profit_status = "positive" if profit >= 0 else "negative"
    cac_today = today['cost'] / today['number_of_customers'] if today['number_of_customers'] else 0
    cac_yesterday = yesterday['cost'] / yesterday['number_of_customers'] if yesterday['number_of_customers'] else 0
    cac_change = ((cac_today - cac_yesterday) / cac_yesterday) * 100 if cac_yesterday else 0
    revenue_change = ((today['revenue'] - yesterday['revenue']) / yesterday['revenue']) * 100 if yesterday['revenue'] else 0
    cost_change = ((today['cost'] - yesterday['cost']) / yesterday['cost']) * 100 if yesterday['cost'] else 0
    return {
        "profit": profit,
        "profit_status": profit_status,
        "cac_today": cac_today,
        "cac_change": cac_change,
        "revenue_change": revenue_change,
        "cost_change": cost_change
    }

def recommendation_node(metrics):
    alerts = []
    recommendations = []
    # هشدار افزایش CAC
    if metrics['cac_change'] > 20:
        alerts.append(f"CAC increased by {metrics['cac_change']:.1f}%")
        recommendations.append("Review marketing campaigns due to significant CAC increase")
    # هشدار سود منفی
    if metrics['profit_status'] == "negative":
        recommendations.append("Reduce costs if profit is negative")
    # توصیه افزایش تبلیغات در صورت رشد فروش
    if metrics['revenue_change'] > 0:
        recommendations.append("Consider increasing advertising budget as sales are growing")
    return {
        "profit": metrics['profit'],
        "profit_status": metrics['profit_status'],
        "alerts": alerts,
        "recommendations": recommendations
    }
