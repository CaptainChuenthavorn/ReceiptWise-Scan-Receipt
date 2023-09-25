import pyautogui
import schedule
import time
import pyperclip
def type_and_enter():
    # Type the desired text
    # pyautogui.typewrite(' ')
    pyperclip.copy("คู่ niulkl6")
    pyautogui.hotkey("ctrl", "v")
    # Press Enter
    pyautogui.press('enter')

def print_message():
    current_time = time.strftime("%H:%M")
    if current_time == "17:37":
        print("It's 17:327! This is your message.")

import sched
from datetime import datetime

s = sched.scheduler()
s.enterabs(datetime(2023, 23, , 17, 58, 48, 0).timestamp(), 1, type_and_enter)
s.enterabs(datetime(2023, 23, 23, 17, 58, 59, 500000).timestamp(), 1, type_and_enter)
s.run()

# # Schedule the job to run at 0:00 AM
# # schedule.every().day.at('17:18:00').do(type_and_enter)
# schedule.every().day.at('17:37:00').do(print_message)

# while True:
#     schedule.run_pending()
#     time.sleep(1)  # Sleep for 1 second to avoid excessive CPU usage
#     # if 