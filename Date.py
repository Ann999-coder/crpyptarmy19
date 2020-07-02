from datetime import date
import time

today = date.today()
print("Today's date:", today)

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print("Current Time:",current_time)