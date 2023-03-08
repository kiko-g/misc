import time
import random
import pyautogui as gui
from termcolor import colored


def move_mouse(start_time, interval_secs=10, move_duration=0.25):
    has_moved = True
    gui.FAILSAFE = False
    print(colored(f"Bot Running in background. Press ctrl + C to exit", "blue"))

    while True:
        elapsed_time = time.time() - start_time
        print("\rElapsed time: {:.2f} seconds".format(elapsed_time), end="")

        if int(elapsed_time) % int(interval_secs) == 0:
            has_moved = False

        if not has_moved:
            x = random.randint(300, 500)
            y = random.randint(400, 600)
            gui.moveTo(x, y, duration=move_duration)
            has_moved = True


if __name__ == "__main__":
    try:
        start_time = time.time()
        move_mouse(start_time)

    except KeyboardInterrupt:
        print(colored(f"\n\nExiting AFK. Lasted {time.time() - start_time} seconds", "red"))
