"""
There are two primary structures in pandas
1. Series: 1-dimensional data structure
2. DataFrame: 2-dimensional data structure
"""

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)

# Calculating the medium temperature:

# using python built-ins
temp_list = data["temp"].tolist()
mean = sum(temp_list) / len(temp_list)
print(mean)

# using pandas
mean = data["temp"].mean()
print(mean)

# ------------------------------------------------------------

max_value = data["temp"].max()
print(max_value)

# ------------------------------------------------------------

# Getting the data from a column

# using python built-ins

print(data["temp"])

# using pandas
print(data.temp)

# ------------------------------------------------------------

# Getting the data from a row

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# Getting the day where the temperature is going to be the lowest

lowtempday = data[data.temp == data.temp.min()].day
print(f"\nDay with the lowest temp:\n{lowtempday}\n")

# ------------------------------------------------------------

sunday = data[data.day == "Sunday"]
sunday_temp = int(sunday.temp)

print(f"Sunday temperature: {sunday_temp} ºC, {sunday_temp * (9 / 5) + 32} ºF\n")

# ------------------------------------------------------------

# Creating a DataFrame from scratch
data_dict = {
    "students": ["Kauã", "Gabriel", "Karlla", "Gabriel"],
    "scores": [9, 9.5, 10, 9]
}
new_df = pandas.DataFrame(data_dict)
print(new_df)
new_df.to_csv("DataFrameToCSV.csv")
