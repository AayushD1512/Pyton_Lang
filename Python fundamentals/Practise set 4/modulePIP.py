import math 

a = math.sqrt(144)
b = math.sin(math.radians(90))
print(a, b)

import requests # pip install requests

a = requests.get("https://api.github.com/")
print(a.json())