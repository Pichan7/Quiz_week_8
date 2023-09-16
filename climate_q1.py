import matplotlib.pyplot as plt
import sqlite3

con = sqlite3.connect("climate.db)
cur = con.cursor()

cur.execute("CREATE TABLE climate(year, co2, temperature)")
cur.execute("""
    INSERT INTO climate VALUES
        (1950, 250, 14.1),
        (1960, 265, 15.5),
        (1970,272,16.3),
        (1980,260,18.1),
        (1990,300,17.3),
        (2000,320,19.1),
        (2010,389,20.2)
""")

con.commit()


                      
        
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
plt.savefig("co2_temp_1.png") 
