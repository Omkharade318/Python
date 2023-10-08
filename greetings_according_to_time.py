import time
t= time.strftime("%H:%M:%S")

hours= int(time.strftime("%H"))
if hours>6 and hours<12:
    print("Good Morning Sir")
elif hours>12 and hours<16:
    print("Good Afternoon Sir")
elif hours>4 and hours<20:
    print("Good Evening sir")
else:
    print ("Good Night Sir, have a good sleep")
print ("The time right now is",t,"sir")

while(hours>0 and hours<6):
    print("You should take a sleep")
    break
