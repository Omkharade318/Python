import time
from plyer import notification

while (True):
    time.sleep(5400)
    notification.notify(title = "Water",
                        message="You should drink water",
                        timeout = 2)    
p= input()    
if quit in p:
    end() 