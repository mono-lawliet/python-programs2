import pyautogui
import time

message = "Hello,"
num_times = 10
delay = 0.1  # Delay in seconds

# Give the user some time to switch to the target application
time.sleep(5)

i = 1 
print (i)

while i < num_times:

    pyautogui.typewrite(message)
    pyautogui.press('enter')
    time.sleep(delay)
    i +=1

