"""
with open("weather_data.csv") as data:
    data_collected = data.readlines()

data_collected = [data.strip() for data in data_collected]

print(data_collected)

---

import csv

with open("weather_data.csv") as file:
    data = csv.reader(file)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))

print(temperature)
"""


