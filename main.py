from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import detect_intent
from fixpriority import analyze_complaint

app = FastAPI()

user_state = {}

class ChatRequest(BaseModel):
    message: str
    user_id: str
   

@app.post("/chat")
def chat(req: ChatRequest):

    intent = detect_intent(req.message)

    if req.user_id not in user_state:
        user_state[req.user_id] = {}

    state = user_state[req.user_id]

    # FILE COMPLAINT
    if intent == "file_complaint":
        state["type"] = req.message
        return {"reply": "Please provide the location."}

    # LOCATION
    elif intent == "provide_location":
        state["location"] = req.message

        result = analyze_complaint(state)

        return {
            "reply": f"Priority: {result['priority']}\nDepartment: {result['department']}\nReason: {result['reason']}"
        }

    # EXPLAIN
    elif intent == "explain_priority":
        return {"reply": "Priority depends on severity, location, and public impact."}

    # GREETING
    elif intent == "greeting":
        return {"reply": "Hello! You can report issues like 'garbage near school'."}

    return {"reply": "I didn’t understand. Try 'pothole near road'."}
