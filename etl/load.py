import pyodbc
import json
import os

# Azure SQL Connection
SERVER = "project62216.database.windows.net"
DATABASE = "project62216"
USERNAME = "sushmaevs"
PASSWORD = "Sushma@2025"
DRIVER="{ODBC Driver 17 for SQL Server}"

def load_to_sql():
    # Connect to SQL Server
    conn = pyodbc.connect(f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}")
    cursor = conn.cursor()

    # Read JSON data from Blob Storage
    with open("weather_data.json", "r") as f:
        data = json.load(f)

    city = data["name"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    # Insert into SQL Table
    cursor.execute("INSERT INTO WeatherData (city, temperature, humidity, description) VALUES (?, ?, ?, ?)", 
                   (city, temperature, humidity, description))
    conn.commit()
    print("Data loaded into Azure SQL Database")

if __name__ == "__main__":
    load_to_sql()
