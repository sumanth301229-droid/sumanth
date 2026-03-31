import datetime
import time

def medication_alert(medicine, schedule_time):
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == schedule_time:
            print(f" Take {medicine} now!")
            return f" Take {medicine} now!"
        print("waiting...current time:", now)
        time.sleep(0)

print(medication_alert("Paracetamol", "09:00"))
