import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

fur_dict = {
    "Fur": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

our_squirrel_data = pandas.DataFrame.from_dict(fur_dict)
print(our_squirrel_data)

