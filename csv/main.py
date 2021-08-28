import csv
import pandas
# with open("weather_data.csv") as data:
#     lines = csv.reader(data)
#     temperatures = []
#     next(data)
#     for row in lines:
#         temperatures.append(int(row[1]))
# print(temperatures)
# temperatures = []
# data = pandas.read_csv("weather_data.csv")
# listoftemps = data["temp"].tolist()
# avgtemp = data.temp.mean()
# maxtemp = data["temp"].max()
# print(data.temp.tolist())
# print(data[data.day == "Friday"])

# print(data[data.temp == data.temp.max()])
#
# print(data[data.temp])

# friday = data[data.day == "Friday"]
#
# firday_temp_in_c =int(friday.temp)
# firday_temp_in_f = firday_temp_in_c * 9/5 +32
#
# print(firday_temp_in_f)



data = pandas.read_csv("squirrel_Data.csv")


b_sq= len(data[data["Primary Fur Color"]=="Black"]);
g_sq= len(data[data["Primary Fur Color"]=="Cinnamon"]);
c_sq= len(data[data["Primary Fur Color"]=="Gray"]);

dit = {
    "Fur Color": ["Black","Cinnamon","Gray"],
    "Fur Count": [b_sq, c_sq, g_sq]
}

datas= pandas.DataFrame(dit)
datas.to_csv('my_data.csv')


