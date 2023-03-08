import pyautogui as gui
import random
import time

print("Bot Running in background. Press ctrl + C to exit")

gui.FAILSAFE = False

try:
    start_time = time.time()
    time_interval = 5
    has_moved = True
    
    while True:
        elapsed_time = time.time() - start_time
        print("\rElapsed time: {:.2f} seconds".format(elapsed_time), end="")
        
        if int(elapsed_time) % int(time_interval) == 0:
            has_moved = False
            
        if not has_moved:
            x = random.randint(300, 500)
            y = random.randint(400, 600)
            gui.moveTo(x, y, duration=1.0)
            has_moved = True

except KeyboardInterrupt:
    print(f"\n\nExiting AFK. Lasted {time.time() - start_time} seconds")
