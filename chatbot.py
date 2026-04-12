def detect_intent(message):
    msg = message.lower()

    if "garbage" in msg or "pothole" in msg or "electric" in msg:
        return "file_complaint"

    elif "near" in msg or "location" in msg:
        return "provide_location"

    elif "why" in msg or "priority" in msg:
        return "explain_priority"

    elif "hi" in msg or "hello" in msg:
        return "greeting"

    return "fallback"