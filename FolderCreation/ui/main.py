import os
import datetime

today = datetime.datetime.now()
# dd/mm/YY
folder = today.strftime("%B_%d-%m-%Y__%H-%M-%S")

print(f"Hey now time is : {folder}")