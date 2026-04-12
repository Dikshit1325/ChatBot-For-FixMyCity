def analyze_complaint(state):
    text = state.get("type", "").lower()
    location = state.get("location", "").lower()

    # TYPE
    if "garbage" in text:
        department = "Sanitation"
        severity = 7
    elif "pothole" in text:
        department = "Public Works"
        severity = 6
    else:
        department = "Electricity Board"
        severity = 8

    # LOCATION
    if "school" in location:
        location_score = 9
    elif "hospital" in location:
        location_score = 10
    else:
        location_score = 5

    # IMPACT
    impact = 8

    score = (severity * 0.4) + (location_score * 0.3) + (impact * 0.3)

    if score > 8:
        priority = "HIGH"
    elif score > 6:
        priority = "MEDIUM"
    else:
        priority = "LOW"

    return {
        "priority": priority,
        "department": department,
        "reason": "High impact area and safety concern"
    }