import pandas

data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
# print(data)
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrel_count, red_squirrel_count, black_squirrel_count)

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("count_squirrels.csv")