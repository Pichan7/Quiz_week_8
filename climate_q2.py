import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r".\2810ICT-7810ICT-Assignment/Quiz_week_8/climate.csv")
df.index = [f'{i}' for i in range(len(df.index))]

df = pd.DataFrame(
    {
        "Year": [
            "1950", "1960", "1970", "1980", "1990", "2000", "2010"
        ],
        "Co2": ["250", "265", "272", "260", "300", "320", "389"],
        "Temperature": ["14.1", "15.5", "16.3", "18.1", "17.3", "19.1", "20.2],
    }
)

years = []
co2 = []
temp = []

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 


