from datetime import datetime
from modal import (
    wsgi_app
)

app = App("dateTime")

current = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("Current local date and time:", current)

