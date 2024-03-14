# Using just file methods
with open("weather_data.csv") as data_file:
    # Read all lines from the file and store them in the 'data' list
    data = data_file.readlines()
    # Print the data
    print(data)

# Using csv library
import csv

with open("weather_data.csv") as data_file:
    # Create a CSV reader object
    data = csv.reader(data_file)
    temperatures = []
    # Iterate through each row in the CSV file
    for row in data:
        # Exclude the header row and append temperatures to the list
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    # Print the list of temperatures
    print(temperatures)

# Using the pandas library
import pandas

# Read the CSV file into a pandas DataFrame
data = pandas.read_csv("weather_data.csv")
# Print the type of the DataFrame
print(type(data))
# Print the type of the 'temp' column in the DataFrame
print(type(data["temp"]))

# Convert the DataFrame to a dictionary
data_dict = data.to_dict()
# Print the dictionary
print(data_dict)

# Convert the 'temp' column to a list
temp_list = data["temp"].to_list()
# Print the length of the list
print(len(temp_list))

# Print the mean and max temperature from the 'temp' column
print(data["temp"].mean())
print(data["temp"].max())

# Get Data in Columns using column names
print(data["condition"])
# Another way to get data in columns using attribute-like access
print(data.condition)

# Get Data in Row where 'day' is 'Monday'
print(data[data.day == "Monday"])

# Get Row where temperature is the maximum temperature
print(data[data.temp == data.temp.max()])

# Get the temperature value for Monday and convert to Fahrenheit
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
# Print the converted temperature for Monday
print(monday_temp_F)

# Create a DataFrame from scratch and write it to a new CSV file
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

# Central Park Squirrel Data Analysis
import pandas

# Read the Central Park Squirrel Census data into a DataFrame
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Count the number of squirrels for each fur color
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

# Print the counts for each fur color
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

# Create a new DataFrame with fur color and corresponding counts, then write to a new CSV file
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")








