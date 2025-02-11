import webbrowser
import time

url = "https://bilheteira.fpf.pt/"

for i in range(30):
    webbrowser.open_new_tab(url)
    time.sleep(1)
