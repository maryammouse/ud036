import webbrowser
import time


i = 1
print("This program started on " + time.ctime())

while i <= 3:
    time.sleep(10)
    webbrowser.open("http://youtu.be/MsicAcvyraM")
    i += 1
