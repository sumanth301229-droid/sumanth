def health_chatbot(user_input):
    user_input = user_input.lower()

    if "fever" in user_input:
        return "Stay hydrated and monitor temperature."
    elif "bp" in user_input:
        return "Normal BP is around 120/80."
    elif "medicine" in user_input:
        return "Take medicines on time."
    else:
        return "Please consult a doctor for detailed advice."

print(health_chatbot("I have fever"))