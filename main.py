from datetime import datetime
app_2 = modal.App()
current = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("Current local date and time:", current)

