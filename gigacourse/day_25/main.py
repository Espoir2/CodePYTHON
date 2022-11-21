import csv
import pandas

with open("weather-data.csv") as data_file:
    data_basics = data_file.readlines()
    print(data_basics)

print("=" * 50)
with open("weather-data.csv") as data_file:
    data_csv = csv.reader(data_file)
    temperatures = []
    for row in data_csv:
        print(row)
        if row[1].isdigit():
            temperatures.append(int(row[1]))
    print(temperatures)


print("=" * 50)
# Read CSV file with pandas
data_pandas = pandas.read_csv("weather-data.csv")
print(type(data_pandas))    # pandas DataFrame
print(data_pandas)
print("*" * 20)
print(type(data_pandas["temp"]))    # pandas Series
print(data_pandas["temp"])
print("*" * 20)

# Convert a CSV file to a dict with pandas
data_pandas_dict = data_pandas.to_dict()
print(data_pandas_dict)
print("*" * 20)

# Convert a CSV file column to a list with pandas
data_pandas_list = data_pandas["temp"].to_list()
print(data_pandas_list)
print("*" * 10, "Average temp", "*" * 10)
# pandas Series function (.mean(), .max())
average_temp = sum(data_pandas_list)/len(data_pandas_list)
print(f"The average of temp is {average_temp:.2f}")
print(f"The average of temp with pandas is {data_pandas['temp'].mean():.2f}")
print(f"The max of temp is {data_pandas['temp'].max()}")

# Get data in column with pandas
# print(data_pandas["condition"])
print(data_pandas.condition)

# Get data in row with pandas
print(data_pandas[data_pandas.day == "Monday"])

# Print the row of data which had the highest temperatures
print(data_pandas[data_pandas.temp == data_pandas.temp.max()])

# Get a row  as variable
monday = data_pandas[data_pandas.day == "Monday"]
print(type(monday))
for element in monday:
    print(monday[element])

# Get monday's temperature in fahrenheit
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a dataframe from scratch

data_dict = {
    "students": ["Espoir", "Nahim", "Vladimir"],
    "score": [100, 200, 300],
}

data_dataframe = pandas.DataFrame(data_dict)
print(data_dataframe)
data_dataframe.to_csv("new_csv_file")


