from datetime import datetime

app = App()

current = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("Current local date and time:", current)

