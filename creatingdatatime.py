import datetime

def medication_alert(medicine, schedule_time):
    now = datetime.datetime.now().strftime("%H:%M")
    if now == schedule_time:
        return f" Take {medicine} now!"
    return "paracetamol"

print(medication_alert("Paracetamol", "10:00"))