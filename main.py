import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_dict = data.to_dict()
print(data_dict['Primary Fur Color'])
gray_sq = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_sq = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_sq = len(data[data["Primary Fur Color"] == "Black"])
new_data = {
    "Colors": ["Gray", "Cinnamon", "Black"],
    "Count":    [gray_sq, cinnamon_sq, black_sq]

}
print(new_data)

df = pandas.DataFrame(new_data)
df.to_csv("squirrel_count.csv")
print(df)
