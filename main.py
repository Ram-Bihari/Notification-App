import time
from win10toast import ToastNotifier

my_notification = ToastNotifier()

for i in range(1, 51):
    my_notification.show_toast("Alert!", "Stop using the laptop and take a break for 10 mins!")
    time.sleep(5400)