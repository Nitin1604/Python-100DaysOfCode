# Day 99

from win10toast import ToastNotifier
toast = ToastNotifier()
toast.show_toast(
    "Notification",
    "Drink Water !!",
    duration = 20,
    icon_path = "icon.ico",
    threaded = True,
)
